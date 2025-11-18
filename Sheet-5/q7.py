a=[1,2,3,45,6]
odd=[x for x in a if x%2 !=0]
even=[x for x in a if x%2==0]
print(*odd)
print(*even)