Checkeven = lambda No : (No % 2 == 0)    # add the function lambda
       
def main():

    Value = int(input("Enter Number :"))

    Ret = Checkeven(Value)    #Ret = (Value % )
    if(Ret == True):
        print("Its Even number :")
    else:
        print("Its Odd number")


if __name__ == "__main__":
    main()
