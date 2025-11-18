#given an array compute the sum of all the elements in the array
def sum(arr):
    total=0
    for i in arr:
        total+=i
    return total
inputs=input("enter the number of space")
arr=list(map(int,inputs.split()))
print(sum(arr))


