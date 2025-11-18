# For every substring check if it is a palindrome or not and get the maximum length.
def palindrome(s):
    n=len(s)
    max_length=1
    for i in range(n):
        for j in range(i,n):
            flag = 1
            for k in range(0,((j-1))//2+1):
                if(s[i+k] != s[j-k]):
                    flag=0
                    if flag ==1 and (j-i+1)>max_length:
                        max_length=j-i+1
    return max_length
s=input("Enter the string:")
print("Length of longest palindromic substring is:",palindrome(s))
