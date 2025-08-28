year =int(input("Enter the year "))
if (year%4==0 and year %100!=0) or (year %400==0):
    print(f"{year}this is leap year ")
else:
    print(f"{year}this is not an leap year ")