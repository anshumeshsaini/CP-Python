#Given N and I, check the i'th bit is set or not(set = 1, unset = 0).
N=12
I=2
if (N & (1 << I)):
    print("Set Bit")
else:
    print("Unset Bit")