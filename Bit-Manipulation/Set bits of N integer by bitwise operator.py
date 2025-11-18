# given an integer n, count how many set bits are there in the N.
N=4
count = 0
while N:
    count += N & 1
    N >>= 1
    print(count)