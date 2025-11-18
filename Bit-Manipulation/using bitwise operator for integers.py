#Given an array of N integers, where all the numbers occurs  an even number of times except 1 number. which occurs an odd number of times. 
# find the number. first line of input contain input N
# denotiong the size of array , next line of he input contain N space seperated integer denoting the element of the array.
N=int(input("Enter the number of elemenyts:"))
arr=list(map(int,input("Enter elemnts seperated by space:").split()))
odd=0
for i in arr:
    odd ^= i
print("odd:",odd)