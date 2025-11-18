def reverse_strings(s):
    if len(s) == 0:
        return ""
    return reverse_strings(s[1:]) + s[0]
s=input("Enter string:")
print(reverse_strings(s))