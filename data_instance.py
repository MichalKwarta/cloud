from typing import TypedDict


class Base_data_instance(TypedDict):

    invalid_attribute_message:list[str]|None
    is_valid:bool|None



class Cloud_data_instance(Base_data_instance): 
    resource:str
    region:str
    


