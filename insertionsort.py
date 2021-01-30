import random
def insertionsort(arr):
    i=0
    while i<len(arr):
        j=i
        k=j-1
        while k>=0 and arr[k]>arr[j]:
            swap(arr,j,k)
            j=k
            k=j-1
        i+=1
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

arr=[random.randint(1,100) for i in range(10)]
print(arr)
insertionsort(arr)
print(arr)