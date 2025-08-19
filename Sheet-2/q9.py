N = int(input("enter a number"))
total = 0
temp = N
while temp > 0:
    total += temp % 10
    temp //= 10
print(total)
