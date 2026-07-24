#Multiple level inheritance
class Base1:
    def fun(self):  #instance method
        print("Inside base1 fun")

class Base2:
    def gun(self):  #instance method
        print("Inside base2 gun")

class Derived(Base1, Base2):
    def sun(self):
        print("Inside derived sun")

        
dobj = Derived()

dobj.fun()
dobj.gun()
dobj.sun()

