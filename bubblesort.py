import random
def bubblesort(arr):
    left=0
    while left<len(arr):
        right=len(arr)-1
        while right>left:
            if(arr[right] < arr[right-1]):
                swap(arr,right,right-1)
            right=right-1
        left+=1
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

arr=[random.randint(1,100) for i in range(10)]
print(arr)
bubblesort(arr)
print(arr)