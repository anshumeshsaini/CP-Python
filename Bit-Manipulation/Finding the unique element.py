# given an array elements every element repeats twice except one , find that unique element .
arr = [2,3,5,4,5,3,2]
unique = 0  
for i in arr:
    unique ^= i
print(unique)