#single level inheritance
class Base:
    
    def fun(self):  #instance method
        print("Inside base fun")

class Derived(Base):
    def sun(self):
        print("Inside derived sun")

        
dobj = Derived()

dobj.fun()
dobj.sun()

