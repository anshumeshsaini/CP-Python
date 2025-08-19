A = int(input("enter a number"))
rev = 0
temp = A
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == A:
    print("yes")
else:
    print("no")
