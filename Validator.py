from typing import Callable, TypedDict

from data_instance import Cloud_data_instance

class Validator:
    def __init__(self,field:str,validate_function:Callable[[object],bool],error_message:str):
        self.field = field
        self.validate_function = validate_function
        self.error_message = error_message

    def validate(self,target:TypedDict)->bool:
        return self.validate_function(target[self.field])  
class Cloud_validator(Validator):
    def __init__(self,field:str,validate_function:Callable[[object],bool],error_message:str):
        super().__init__(field,validate_function,error_message)
        if field not in Cloud_data_instance.__annotations__.keys():
            raise ValueError(f"Field {field} is not a valid field for Cloud_data_instance")
    
    