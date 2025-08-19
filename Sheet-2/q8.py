N = int(input("enter a number "))
count = 0
temp = N
while temp > 0:
    count += 1
    temp //= 10
print(count)
