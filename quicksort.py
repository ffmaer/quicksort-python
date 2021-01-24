import random

def quicksort(arr, low, high):
    if low<high:
        pivot = partition(arr,low,high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
def partition(arr, low, high):
    pivot = arr[low]
    #chunk1 less or equal to pivot
    chunk1_last = low
    for i in range(low+1,high+1):
        if arr[i] < pivot:
            swap(arr, chunk1_last+1,i)
            chunk1_last+=1
    swap(arr, low, chunk1_last)
    return chunk1_last
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

arr=[random.randint(1,100) for i in range(10)]
random.shuffle(arr) # shuffle to array to avoid worst case scenario for quicksort
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)