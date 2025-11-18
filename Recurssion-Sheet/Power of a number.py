def power(x,n):
    if n ==0:
        return 1
    return x * power(x, n -1)

x,n= map(int, input("Enter  x and n:").split())
print(power(x,n))