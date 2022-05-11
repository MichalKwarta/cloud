
from Validator import Validator
from data_instance import Base_data_instance
from collections import defaultdict

class Data_model:

    def __init__(self,validators:list[Validator]|None = None):
        
        self.instaces:list[Base_data_instance] = []
        self.validators = validators


    def add_instance(self,instance:Base_data_instance):

        if self.validators:
            validation_messages =  [validator.error_message for validator in self.validators if not validator.validate(instance)]
            instance['invalid_attribute_message'] = validation_messages
            instance['is_valid'] = not validation_messages
        self.instaces.append(instance)
        
        
    def add_many_instances(self,instances:list[Base_data_instance]):

        for instance in instances:
            self.add_instance(instance)

    def generate_validation_raport(self):

        grouped_invalid_instances = defaultdict(list)
        for instance in self.instaces:
            if not instance['is_valid'] and instance['invalid_attribute_message']:
                for message in instance['invalid_attribute_message']:
                    grouped_invalid_instances[message].append(instance)
        return grouped_invalid_instances

    def print_validation_raport(self):

        if not self.instaces:
            print("No instances to generate report for")
            return 

        if raport := self.generate_validation_raport():
            print("Invalid instances found:")
            for error_type,instances in raport.items():
                print(error_type)
                print("-"*len(error_type))
                for instance in instances:
                    print(instance)
                print()
        else:
            print("All instances valid!")



   


    
    

    

    