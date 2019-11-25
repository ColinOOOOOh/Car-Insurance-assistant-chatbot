from pyswip import Prolog, Functor, Variable, Query

class KnowledgeBase:
    def __init__(self, file_path="kb.pl"):
        self.prolog = Prolog()
        self.prolog.consult(file_path)
