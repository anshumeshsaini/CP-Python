#Given a string,calculate the length of longest palindromic substring.
s=input()
best=1
for i in range(len(s)):
    for L,R in ([(i,i),(i,i+1)]):
        while L>=0 and R<len(s) and s[L]==s[R]:
            best = max(best,R-L+1)
            L -= 1
            R += 1
print(best)
