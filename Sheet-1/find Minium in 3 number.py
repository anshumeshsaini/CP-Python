a= float(input("enter the 1st number"))
b= float(input("Enter the 2nd number"))
c=float(input("Enter the 3rd number"))
if a<=b and a<=c:
    print(f"the mini is {a}")
elif b<=a and b<=c:
    print(f"the mini is {b}")
else:
    print(f"{c}")

def square_range(x, y):
    for i in range(x, y + 1):
        print(f"{i}² = {i * i}")

# Taking input from user
x = int(input("Enter starting number (x): "))
y = int(input("Enter ending number (y): "))

square_range(x, y)
