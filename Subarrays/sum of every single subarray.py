N=int(input("Enetr size of array:"))
arr=list(map(int, input("Enter array elements:").split()))
for i in range(N):
    curr_sum=0
    for j in range(i,N):
        curr_sum += arr[j]
        print(curr_sum)