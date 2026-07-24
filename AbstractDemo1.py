from abc import ABC, abstractmethod           #abc = abstract base class

class Base(ABC):    #(ABC) beacause it write the abstract class in base class
    @abstractmethod
    def Addition(self, No1, No2):
        pass



class Derived(Base):
    pass

dobj = Derived()   #Error....
