a=[1,2,3,4,5]
even=sum(1 for x in a if x%2==0)
odd=len(a)-even
print(abs(even-odd))