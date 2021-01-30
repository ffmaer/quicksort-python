import random
def selectionsort(arr):
    i=0
    while i<len(arr):
        swap(arr,i,min_index(arr,i))
        i+=1
def min_index(arr,left):
    min_i=left
    for i in range(left,len(arr)):
        if arr[i]<arr[min_i]:
            min_i=i
    return min_i
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

arr=[random.randint(1,100) for i in range(10)]
print(arr)
selectionsort(arr)
print(arr)