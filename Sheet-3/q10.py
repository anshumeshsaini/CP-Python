for i in range(1,6):
    if i%2!=0:
        print("*".join(str(j) for j in range(1,i+1,2)))
    else:
        print("*".join(str(j) for j in range(1,i,2))+"*")

