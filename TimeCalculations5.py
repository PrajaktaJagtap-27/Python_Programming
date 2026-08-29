# final time calculation
import time

def Factorial(no):
    Fact = 1

    for i in range(1,no+1):
        Fact = Fact * i
    return Fact    

def main():
    Value = int(input("Enter n number :"))
    start_time = time.perf_counter()  #update

    Ret = Factorial(Value)

    end_time = time.perf_counter()    #update

    print(f"Factorial of {Value} is {Ret}")  
    print(f"time requried is :{end_time-start_time:.5f} seconds")
if __name__ == "__main__":
    main()    