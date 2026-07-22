#single level inheritance
class Base:
    def __init__(self):
        print("Inside base constructor")


class Derived(Base):
    def __init__(self):
        super().__init__()     #its access the base class using super keyword
        print("Inside Derived constructor")

bobj = Derived()

