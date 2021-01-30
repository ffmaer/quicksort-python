import random
def countingsort(arr,k):
    #assuming range: [0,k]
    count=[0 for i in range(k+1)]
    for i in range(len(arr)):
        num=arr[i]
        count[num]+=1
    for i in range(1,len(count)):
        count[i]=count[i-1]+count[i]
    new_arr=[None] * len(arr)
    for i in range(len(arr)):
        num=arr[i]
        new_arr[count[num]-1]=num
        count[num]-=1
    for i in range(len(arr)):
        arr[i]=new_arr[i]

k=100
arr=[random.randint(1,k) for i in range(10)]
print(arr)
countingsort(arr,k)
print(arr)