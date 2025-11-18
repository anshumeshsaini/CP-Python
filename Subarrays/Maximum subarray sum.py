N=int(input("Enter size of array:"))
arr = list(map(int, input("Enter array elements: ").split()))

max_sum=arr[0]
curr_sum=arr[0]
for i in range(1,N):
    curr_sum= max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)

print("Maximum Subarray Sum : ", max_sum)