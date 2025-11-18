N=int(input("Enter size of array:"))
arr = list(map(int, input("Enter array elements:").split()))
L,R = map(int, input("Enter L and R:").split())

count= sum(arr[L-1:R])
print("Sum of subaaray:",count)