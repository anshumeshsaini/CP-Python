# given an list of int and a target numver find the and print the index of the target number in the list
def find(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
inputs=input("enter the number of space")
arr=list(map(int,inputs.split()))
target =int(input("enter the targated numnber"))
print(find(arr,target))

