def merge(n=5):
    for i in range(n):
        print("*"*(n-1),end="")
        print(" "*(2*i),end="")
        print("*"*(n-1))
    for i in range(n):
        left = '*' * i
        spaces = ' ' * (2 * (n - i))
        right = "*" * i
        print(left + spaces + right)
    print("*"*(2*n))
merge()

