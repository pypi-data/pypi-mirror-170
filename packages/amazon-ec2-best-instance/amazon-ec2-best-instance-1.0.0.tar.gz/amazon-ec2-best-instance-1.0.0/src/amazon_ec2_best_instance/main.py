import boto3
import subprocess
import json
import logging
from multiprocessing.pool import ThreadPool as Pool
from .SpotUtils import SpotUtils


class Ec2BestInstance:
    __DESCRIBE_SPOT_PRICE_HISTORY_CONCURRENCY = 10
    __DESCRIBE_ON_DEMAND_PRICE_CONCURRENCY = 10

    def __init__(self, options=None, logger=None):
        self.__region = 'us-east-1'
        self.__describe_spot_price_history_concurrency = self.__DESCRIBE_SPOT_PRICE_HISTORY_CONCURRENCY
        self.__describe_on_demand_price_concurrency = self.__DESCRIBE_ON_DEMAND_PRICE_CONCURRENCY
        if options is not None:
            if options.get('region'):
                self.__region = options['region']
            if options.get('describe_spot_price_history_concurrency'):
                self.__describe_spot_price_history_concurrency = options.get('describe_spot_price_history_concurrency')
            if options.get('describe_on_demand_price_concurrency'):
                self.__describe_on_demand_price_concurrency = options.get('describe_on_demand_price_concurrency')
        self.__ec2_client = boto3.client('ec2', region_name=self.__region)
        self.__logger = logger if logger is not None else logging.getLogger()

    def get_best_instance_types(self, options=None):
        import logging
        logging.getLogger("urllib3").setLevel(logging.ERROR)
        if options is None:
            raise Exception('Options are missing')
        if options.get('vcpu') is None:
            raise Exception('A vcpu option is missing')
        if options.get('memory_gb') is None:
            raise Exception('A memory_gb option is missing')

        cpu = options['vcpu']
        memory_gb = options.get('memory_gb')

        usage_class = options.get('usage_class', 'on-demand')
        burstable = options.get('burstable')
        architecture = options.get('architecture', 'x86_64')
        product_descriptions = options.get('operation_systems', ['Linux/UNIX'])
        is_current_generation = None
        is_best_price = options.get('is_best_price', False)
        is_instance_storage_supported = options.get('is_instance_storage_supported')
        max_interruption_frequency = options.get('max_interruption_frequency')

        if options.get('is_current_generation'):
            is_current_generation = 'true' if options['is_current_generation'] == True else 'false'

        instances = self.__describe_instance_types({
            'is_current_generation': is_current_generation,
            'is_instance_storage_supported': is_instance_storage_supported
        })

        filtered_instances = self.__filter_ec2_instances(instances, {
            'cpu': cpu,
            'memory_gb': memory_gb,
            'usage_class': usage_class,
            'burstable': burstable,
            'architecture': architecture
        })

        self.__logger.debug(f'Instance types number before filtering: {str(len(instances))}')

        if usage_class == 'spot' and max_interruption_frequency is not None:
            spot_utils = SpotUtils(self.__region)
            operation_systems = Ec2BestInstance.__get_operation_systems_by_product_descriptions(product_descriptions)

            if len(operation_systems) > 1:
                raise Exception('You must use Windows or Linux OS, not both')

            interruption_frequencies = spot_utils.get_spot_interruption_frequency(operation_systems[0])

            def interruption_frequency_statistic_existing_filter(ec2_instance):
                instance_type = ec2_instance['InstanceType']
                if interruption_frequencies.get(instance_type) is not None:
                    return True
                else:
                    self.__logger.warning(
                        f'Interruption frequency statistic is missing for {instance_type}, so instance type is ignored')
                    return False

            filtered_instances = list(filter(interruption_frequency_statistic_existing_filter, filtered_instances))

            def add_interruption_frequency(ec2_instance, interruption_frequency):
                ec2_instance['interruption_frequency'] = interruption_frequency
                return ec2_instance

            filtered_instances = list(map(lambda ec2_instance:
                                          add_interruption_frequency(ec2_instance, interruption_frequencies[
                                              ec2_instance['InstanceType']]),
                                          filtered_instances))
            filtered_instances = list(
                filter(lambda ec2_instance: ec2_instance['interruption_frequency']['min'] <= max_interruption_frequency,
                       filtered_instances))

        self.__logger.debug(f'Instance types number after filtering: {str(len(filtered_instances))}')

        if is_best_price:
            if usage_class == 'on-demand':
                instance_types = list(map(lambda ec2_instance: ec2_instance['InstanceType'], filtered_instances))
                return [self.__get_best_on_demand_price_instance_type(instance_types)]
            elif usage_class == 'spot':
                return [self.__get_best_spot_price_instance_type(filtered_instances, product_descriptions)]
            else:
                raise Exception(f'The usage_class: {usage_class} does not exist')

        return list(map(lambda ec2_instance: {'instance_type': ec2_instance['InstanceType']}, filtered_instances))

    def is_instance_storage_supported_for_instance_type(self, instance_type):
        response = self.__ec2_client.describe_instance_types(
            InstanceTypes=[instance_type]
        )
        instance_types = response['InstanceTypes']
        if len(instance_types) == 0:
            raise Exception(f'The {instance_type} instance type not found')
        instance_type_description = instance_types[0]
        is_instance_storage_supported = instance_type_description['InstanceStorageSupported']
        return is_instance_storage_supported

    def __describe_instance_types(self, options=None):
        is_current_generation = None
        is_instance_storage_supported = None

        if options is not None:
            is_current_generation = options.get('is_current_generation')
            is_instance_storage_supported = options.get('is_instance_storage_supported')

        instances = []

        response = self.__describe_instance_types_page(
            is_current_generation=is_current_generation,
            is_instance_storage_supported=is_instance_storage_supported
        )

        instances += response['InstanceTypes']

        next_token = response.get('NextToken')

        while next_token is not None:
            response = self.__describe_instance_types_page(next_token, is_current_generation,
                                                           is_instance_storage_supported)
            instances += response['InstanceTypes']
            next_token = response.get('NextToken')

        return instances

    def __describe_instance_types_page(self, next_token=None, is_current_generation=None,
                                       is_instance_storage_supported=None):
        filters = [] if is_current_generation is None else [{
            'Name': 'current-generation',
            'Values': [is_current_generation]
        }]

        if is_instance_storage_supported is not None:
            if is_instance_storage_supported:
                filters.append({
                    'Name': 'instance-storage-supported',
                    'Values': ['true']
                })
            else:
                filters.append({
                    'Name': 'instance-storage-supported',
                    'Values': ['false']
                })

        if next_token is not None:
            response = self.__ec2_client.describe_instance_types(
                Filters=filters,
                NextToken=next_token
            )
        else:
            response = self.__ec2_client.describe_instance_types(
                Filters=filters
            )

        return response

    def __filter_ec2_instances(self, instances, options):
        if options is None:
            return []

        filtered_instances = []

        if options.get('cpu') is not None:
            filtered_instances = list(
                filter(lambda ec2_instance: ec2_instance['VCpuInfo']['DefaultVCpus'] >= options.get('cpu'), instances))
        if options.get('memory_gb') is not None:
            filtered_instances = list(
                filter(lambda ec2_instance: ec2_instance['MemoryInfo']['SizeInMiB'] >= options.get('memory_gb') * 1024,
                       filtered_instances))
        if options.get('usage_class') is not None:
            filtered_instances = list(
                filter(lambda ec2_instance: options.get('usage_class') in ec2_instance['SupportedUsageClasses'],
                       filtered_instances))
        if options.get('burstable') is not None:
            filtered_instances = list(
                filter(lambda ec2_instance: options.get('burstable') == ec2_instance['BurstablePerformanceSupported'],
                       filtered_instances))
        if options.get('architecture') is not None:
            filtered_instances = list(
                filter(lambda ec2_instance: options.get('architecture') in ec2_instance['ProcessorInfo'][
                    'SupportedArchitectures'],
                       filtered_instances))

        return filtered_instances

    def __ec2_instance_price_loop(self, ec2_instance, product_descriptions, best_spot_price_instance_type_data):
        instance_type = ec2_instance['InstanceType']

        response = self.__ec2_client.describe_spot_price_history(
            InstanceTypes=[instance_type],
            Filters=[
                {
                    'Name': 'product-description',
                    'Values': product_descriptions
                }
            ]
        )

        spot_price = response['SpotPriceHistory'][0]['SpotPrice']

        if spot_price < best_spot_price_instance_type_data.best_instance['price']:
            best_spot_price_instance_type_data.best_instance = {
                'price': spot_price,
                'ec2_instance': ec2_instance,
                'spot_price_history': response['SpotPriceHistory'][0]
            }

    def __get_best_spot_price_instance_type(self, filtered_instances, product_descriptions):
        class BestSpotPriceInstanceTypeData:
            def __init__(self):
                self.best_instance = {
                    'price': '10000.0'
                }

        pool = Pool(self.__describe_spot_price_history_concurrency)

        best_spot_price_instance_type_data = BestSpotPriceInstanceTypeData()

        for ec2_instance in filtered_instances:
            pool.apply_async(self.__ec2_instance_price_loop,
                             (ec2_instance, product_descriptions, best_spot_price_instance_type_data))

        pool.close()
        pool.join()

        interruption_frequency = best_spot_price_instance_type_data.best_instance['ec2_instance'] \
            .get('interruption_frequency')

        entry = {
            'instance_type': best_spot_price_instance_type_data.best_instance['ec2_instance']['InstanceType'],
            'price': best_spot_price_instance_type_data.best_instance['price']
        }

        if interruption_frequency:
            entry['interruption_frequency'] = interruption_frequency

        return entry

    def __get_best_on_demand_price_instance_type(self, instance_types):
        pool = Pool(self.__describe_on_demand_price_concurrency)

        prices = []

        for instance_type in instance_types:
            pool.apply_async(self.__get_on_demand_price_instance_type, (instance_type, prices))

        pool.close()
        pool.join()

        sorted_prices = sorted(prices, key=lambda price: price['price'])

        return {
            'instance_type': sorted_prices[0]['instance_type'],
            'price': sorted_prices[0]['price']
        }

    def __get_on_demand_price_instance_type(self, instance_type, prices):
        result = subprocess.check_output(["curl", "-sL", f"ec2.shop?filter={instance_type}", "-H", "accept:json"])
        response_string = str(result).replace("b'", "").replace("\\n'", "")
        response_dict = json.loads(response_string)
        prices.append({
            'price': response_dict['Prices'][0]['Cost'],
            'instance_type': instance_type
        })

    @staticmethod
    def __get_operation_systems_by_product_descriptions(product_descriptions):
        # Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)
        return Ec2BestInstance.unique(
            ['Linux' if product_description in ['Linux/UNIX', 'Linux/UNIX (Amazon VPC)'] else 'Windows' for
             product_description in product_descriptions])

    @staticmethod
    def unique(list1):
        list_set = set(list1)
        unique_list = (list(list_set))
        return unique_list
