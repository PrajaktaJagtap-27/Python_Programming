def Checkeven(No):
    if(No % 2 == 0):
        print("Its Even number")
    else:
        print("Its odd number")


def main():

    Value = int(input("Enter Number :"))

    Checkeven(Value)


if __name__ == "__main__":
    main()
