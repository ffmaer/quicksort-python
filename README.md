# Sort x Python

## Implementing Sorting Algorithms in Python

### QuickSort
- We randomize the array before sorting to avoid worst-case performance.
- We always choose the first element in the partition to be the pivot.

### MergeSort
- We used the bottom-up approach.
- We used a third array of size n to help with merging two subarrays of size n/2.

### HeapSort
- We used a max-heap.

### SelectionSort
- In every iteration, we select the minimum from the unsorted and put it in the right place.

### InsertionSort
- In every iteration, we insert a new number into the sorted numbers.

### BubbleSort
- BubbleSort works because we will move the smallest discovered to the left one step at a time.

### CountingSort
- When the range of input is large, CountingSort may take a huge amount of space.
- It's useful when the input has a small amount of variety within a small range. And the input range can be mapped to array indices easily.

### PigeonHoleSort
- While CountingSort only uses an auxiliary array to keep track of the counts, PigeonHoleSort creates an auxiliary array to store numbers, or perhaps references to objects (for example, pigeons). [5]

### BucketSort
- It's a scatter-gather approach. [1]
- [Visualizations](https://medium.com/karuna-sehgal/an-introduction-to-bucket-sort-62aa5325d124)
- "The worst-case scenario occurs when all the elements are placed in a single bucket. The overall performance would then be dominated by the algorithm used to sort each bucket." [3]

### RadixSort
- "Radix is a Latin word for 'root'. 'Root' can be considered a synonym for base, in the arithmetical sense." [4] Base-10-sort, alphabet-sort.
- Sort digit by digit from the most significant bit to the least significant bit or from the least significant bit to the most significant bit.

### Bogosort
- It's also known as monkey sort, stupid sort, random sort, and permutation sort. [2]
- It's a highly inefficient sorting algorithm. [2]

### Pancakesort
- Time: O(n^2) Space: O(1)
- You find and flip the largest element to the front. And then you flip the largest element to the end. Repeat the process until the arry is sorted.

References:
1. https://www.programiz.com/dsa/bucket-sort
2. https://en.wikipedia.org/wiki/Bogosort
3. https://en.wikipedia.org/wiki/Bucket_sort
4. https://en.wikipedia.org/wiki/Radix
5. https://en.wikipedia.org/wiki/Pigeonhole_sort