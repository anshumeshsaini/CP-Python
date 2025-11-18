N=int(input("Enter size of array:"))
arr = list(map(int, input("Enter array elements: ").split()))

total_sum = 0
for i in range(N):
    contribution = arr[i] * (i+1) * (N-i)
    total_sum += contribution

print("Sum of all subarrays sums: ", total_sum)