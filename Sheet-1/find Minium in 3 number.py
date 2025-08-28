a= float(input("enter the 1st number"))
b= float(input("Enter the 2nd number"))
c=float(input("Enter the 3rd number"))
if a<=b and a<=c:
    print(f"the mini is {a}")
elif b<=a and b<=c:
    print(f"the mini is {b}")
else:
    print(f"{c}")