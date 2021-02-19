import math
def pancake_sort(arr):
  def flip(arr,k):
    i=0
    j=k-1
    while i<j:
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      i+=1
      j-=1
  
  def findMax(arr,end_index):
    max_one = -math.inf
    max_one_index = -1
    i=0
    while i<=end_index:
      if arr[i]>max_one:
          max_one = arr[i]
          max_one_index=i
      i+=1
    return max_one,max_one_index
  end_index = len(arr)-1
  while end_index>0:    
    max_one,max_one_index = findMax(arr,end_index)
    flip(arr, max_one_index+1)
    flip(arr, end_index+1)
    end_index-=1
  
  return arr

print(pancake_sort([3,2,2,1,1]))