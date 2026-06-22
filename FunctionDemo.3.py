
from Marvellous import Addition   #update 

def main():
    print("Enter first  number : ")
    Value1 = int(input())
    
    print("Enter first  number : ")
    Value2 = int(input())

    Ret = Addition(Value1 , Value2) 
    print("Addition is :",Ret)

    Ret = Substraction(Value1,Value2) #update   Error
    print("Substraction is :",Ret)

if __name__ =="__main__":   
    main()
    
