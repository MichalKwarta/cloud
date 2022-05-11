import json
from Data_model import Data_model

from data_instance import Cloud_data_instance
from Validator import Cloud_validator 
 
with open('data.json') as json_file:
    data = [Cloud_data_instance(**instance) for instance in json.load(json_file)]



valid_resources = ["iam", "cdn", "ec2","s3"]
valid_regions = ["eu-central-1", "us-west-1", "us-east-2"]

region_validator = Cloud_validator("region",lambda x: x in valid_regions,"Invalid region")
resource_validator = Cloud_validator("resource",lambda x: x in valid_resources,"Invalid resource")

cloud_data_aggregator = Data_model(validators=[region_validator,resource_validator])
cloud_data_aggregator.add_many_instances(data)  # type: ignore 
cloud_data_aggregator.print_validation_raport()