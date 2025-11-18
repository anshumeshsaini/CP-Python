a = int(input("enter a number + number "))
divisor =[]
for i in range(1,a+1):
    if a%i==0:
        divisor.append(i)
        print("divisor",a,":",*divisor)

