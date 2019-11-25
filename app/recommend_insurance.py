from typing import List
from app.kb import KnowledgeBase

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

    def __repr__(self) -> str:
        return str((self.identifier, 
                    self.name,
                    self.coverage,
                    self.duration,
                    self.price,
                    self.price_range))

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

    def __repr__(self) -> str:
        return str((self.occupation, 
                    self.age,
                    self.car_model,
                    self.prev_accidents))

def RecommendInsurance(kb: KnowledgeBase,
                       user_features: UserFeatures) -> List[Insurance]:
    query_results = kb.Pick(occupation=user_features.occupation,
                      age=user_features.age,
                      prev_accidents=user_features.prev_accidents,
                      car_model=user_features.car_model)

    recommendations = list()
    for identifier, name, coverage, duration, price, price_range in query_results:
        recommendations.append(
                Insurance(identifier=identifier, 
                          name=name, 
                          coverage=coverage, 
                          duration=duration, 
                          price=price, 
                          price_range=price_range))

    return recommendations

if __name__ == "__main__":
    insurances = RecommendInsurance(KnowledgeBase("kb.pl"),
                                    UserFeatures("engineer", 32, "toyota_corolla", 1))
    print(insurances)
