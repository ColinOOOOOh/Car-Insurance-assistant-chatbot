from typing import Tuple, Set
from pyswip import Prolog, Functor, Variable, Query

class KnowledgeBase:
    def __init__(self, file_path="kb.pl"):
        self.prolog = Prolog()
        self.prolog.consult(file_path)

    def Pick(self,
             occupation: str, 
             age: int, 
             prev_accidents: int, 
             car_model: int) -> Set[Tuple[int, str, str, int, float, str]]:
        INSURANCE_ID, INSURANCE_TYPE, INSURANCE_COVERAGE, \
        INSURANCE_DURATION, INSURANCE_PRICE, INSURANCE_PRICE_RANGE = \
            Variable(), Variable(), Variable(), Variable(), Variable(), Variable()
        fpick = Functor("pick", 10)

        query = Query(fpick(occupation, age, prev_accidents, car_model, 
                            INSURANCE_ID, INSURANCE_TYPE, INSURANCE_COVERAGE,
                            INSURANCE_DURATION, INSURANCE_PRICE, INSURANCE_PRICE_RANGE))

        results = set()
        while query.nextSolution():
            results.add((INSURANCE_ID.value, 
                         str(INSURANCE_TYPE.value),
                         str(INSURANCE_COVERAGE.value),
                         INSURANCE_DURATION.value,
                         INSURANCE_PRICE.value,
                         str(INSURANCE_PRICE_RANGE.value)))
        query.closeQuery()

        return results

