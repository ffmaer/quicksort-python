import random
import math

def heapsort(arr):
    global heap
    heap=['-']
    heapify(arr)
    sorted_arr=[]
    while(len(heap)>1):
        sorted_arr.append(removeMax())
    sorted_arr.reverse()
    for i in range(len(arr)):
        arr[i]=sorted_arr[i]

def heapify(arr):
    for i in range(len(arr)):
        insert(arr[i])

def removeMax():
    last=len(heap)-1
    max_val = heap[1]
    heap[1]=heap[last]
    heap.pop(-1)
    parent=1
    left=2*parent
    right=2*parent+1
    while (left<len(heap) and heap[parent]<heap[left]) or (right<len(heap) and heap[parent]<heap[right]):
        if right<len(heap) and heap[left]<heap[right]:
            swap(parent,right)
            parent=right
        else:
            swap(parent,left)
            parent=left
        left=2*parent
        right=2*parent+1
    return max_val

def insert(element):
    heap.append(element)
    n=len(heap)-1 #last index
    parent=math.floor(n/2)
    while parent>=1 and heap[parent]<heap[n]:
        swap(parent,n)
        n=parent
        parent=math.floor(n/2)

def swap(i,j):
    temp=heap[i]
    heap[i]=heap[j]
    heap[j]=temp

arr=[random.randint(1,100) for i in range(10)]
print(arr)
heapsort(arr)
print(arr)