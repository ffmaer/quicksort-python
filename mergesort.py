# Bottom-up MergeSort
# Time: O(nlogn)
# Space: O(n)

import random

def mergesort(arr):
    aux=[0 for i in range(len(arr))]
    size=2
    while size/2<len(arr):
        low=0
        while low<len(arr)-1:
            mid=low+size/2
            high=min(len(arr)-1,low+size-1)
            if mid > len(arr)-1: break
            merge(arr, low, mid, high, aux) # [low, mid-1] [mid, high]
            low+=size
        size*=2

def merge(arr, low, mid, high, aux):
    i=low
    j=mid
    for k in range(low, high+1):
        if i>mid-1:
            aux[k]=arr[j]
            j+=1
        elif j>high:
            aux[k]=arr[i]
            i+=1
        elif arr[i]<arr[j]:
            aux[k]=arr[i]
            i+=1
        else:
            aux[k]=arr[j]
            j+=1
    for k in range(low, high+1):
        arr[k]=aux[k]

arr=[random.randint(1,100) for i in range(10)]
print(arr)
mergesort(arr)
print(arr)