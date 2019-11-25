from typing import List
from kb import KnowledgeBase

class Insurance:
    def __init__(self, 
                 identifier: int, 
                 name: str, 
                 coverage: str, 
                 duration: int,
                 price: float,
                 price_range: str):
        self.identifier = identifier 
        self.name = name 
        self.coverage = coverage 
        self.duration = duration 
        self.price = price 
        self.price_range = price_range

class UserFeatures:
    def __init__(self,
                 occupation: str,
                 age: int,
                 car_model: str,
                 prev_accidents: int):
       self.occupation = occupation 
       self.age = age
       self.car_model = car_model
       self.prev_accidents = prev_accidents

def RecommendInsurance(kb: KnowledgeBase,
                       user_features: UserFeatures) -> List[Insurance]:
    pass

