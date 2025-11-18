N=int(input("Enter size of array:"))
arr = list(map(int, input("Enter array elememts:").split()))
for i in range(N):
    for j in range(i,N):
        print(*arr[i:j+1])