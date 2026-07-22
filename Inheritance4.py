#single level inheritance
class Base:
    def __init__(self):
        print("Inside base constructor")

    def fun(self):  #instance method
        print("Inside base fun")

class Derived(Base):
        pass
        
dobj = Derived()

dobj.fun()

