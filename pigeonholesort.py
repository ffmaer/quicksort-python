import random
def pigeonholesort(arr,k):
    #assuming range: [0,k]
    holes=[[] for i in range(k+1)]
    for i in range(len(arr)):
        num=arr[i]
        holes[num].append(num)
    new_arr=[]
    for i in range(1,len(holes)):
        new_arr+=holes[i]
    for i in range(len(arr)):
        arr[i]=new_arr[i]

k=100
arr=[random.randint(1,k) for i in range(10)]
print(arr)
pigeonholesort(arr,k)
print(arr)