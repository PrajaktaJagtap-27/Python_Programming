class Demo:
    # class variables 
   Value1 = 10
   Value2 = 20

   def __init__(self):
     self.No1 = 11
     self.No2 = 21

   #Instance method   it access the all
   def fun(self):
     print("Inside instance method  named as fun")
     print(self.No1)
     print(self.No2)

     print(self.Value1)
     print(self.Value2)

   @classmethod
   def gun(cls):
     print("Inside the ")
     #print(Demo.No1)
     #print(Demo.No2)
     print(Demo.Value1)
     print(Demo.Value2)

#call with object

dobj = Demo()
dobj.gun()

