def pattren(n=5):
    for i in range(n):
        left = '*' * i
        spaces = ' ' * (2 * (n - i))
        right ="*"*i
        print(left+spaces+right)
    print("*"*(2*n))
pattren()

