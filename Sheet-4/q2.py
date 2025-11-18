# using indexing
num=[22,44,55,66,22]
num[::-1]
print(num)

#using reverse()
num=[2,4,5,6,2]
num.reverse()
print(num)

#using reversed()
nums = [222, 443, 553, 662, 223]
rev = list(reversed(nums))
print(rev)
print(nums)

#using reversed()
nums=[3,4,5,6,7,8,9]
rev=[]
for x in reversed(nums):
    rev.append(x)
print(rev)

#swapping
list1=[1,2,4,54,6,67,7,8,89]
N=len(list1)q
for i in range(0, N//2):
    list1[i], list1[N-i-1] = list1[N-i-1], list1[i]
print(list1)

#using split
str1="Anshumesh-saini"
print(str1.split("-"))
str1="123456765432"
print(str1.split(" "))
sb= list(map)(int.input().split())
print(sb)
n=map(int,input().split())
print(n)




