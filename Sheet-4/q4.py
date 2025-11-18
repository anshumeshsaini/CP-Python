def find(arr):
    if not arr:
        return None
    maxelement=arr[0]
    for num in arr:
        if num>maxelement:
            maxelement=num
    return maxelement
num=[1,2,3,4,6,7]
result=find(num)
print(f"max element of the arrary{result}")

