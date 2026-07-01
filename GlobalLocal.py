
no = 11                # Global variable

def Display():
    a = 21     # local variable
    print("From display : ",no)
    print("From display value of a is : ",a) 
    

def Demo():
    print("From display value of a is : ",a) #error
    print("From demo : ",no)

Display()      #call of function 
Demo()
