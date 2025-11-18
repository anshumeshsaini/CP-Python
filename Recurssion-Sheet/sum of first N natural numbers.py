def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
n=int(input("enter N:"))
print(sum(n))