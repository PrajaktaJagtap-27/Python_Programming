print("Enter the sixe of array")
size = int(input())

#int *Arr = (int *)malloc(sizeof(int) * size)
#int Arr[] = new int[size]; c++
#int Arr[] = new int[size]; java
Arr = [0] * size

print("Size of array is :",len(Arr))
print(Arr[0])
print(Arr[1])
print(Arr[2])
print(Arr[3])

del Arr