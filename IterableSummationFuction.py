def Summation(Data):
    Sum = 0

    for no in Data:      
        Sum = Sum + no    #update to addition of numbers

    return Sum

def main():
    Marks = [78,90,56,98,77]
    Ret = Summation(Marks)

    print("Addtion is : ",Ret)

if __name__ == "__main__":
    main()
