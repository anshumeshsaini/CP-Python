#given an array and a target number find number of occurrences of the target number in the array
def count(arr,target):
    count =0
    for i in arr:
        if i==target:
            count+=1
    return count
inputs=input("enter the number of space")
arr=list(map(int,inputs.split()))
target=int(input("Enter the targeted number"))
print(count(arr,target))


