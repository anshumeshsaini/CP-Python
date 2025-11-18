# given an array and an increment number , genrate a new array which contian all values of orignal array increase by increment value
def increase(arr,incremnt):
    new_arr=[]
    for i in arr:
        new_arr.append(i+incremnt)
    return new_arr
inputs=input("enter the numbe of space")
arr=list(map(int,inputs.split()))
incremnt=int(input("enter the incremented value"))
print(increase(arr,incremnt))


