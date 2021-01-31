## Sort x Python: Implementing Sorting Algorithms in Python

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

### BogoSort
- It's also known as monkey sort, stupid sort, random sort, and permutation sort. [2]
- It's a highly inefficient sorting algorithm. [2]

### ShellSort
- The algorithm was published in 1959 and was named after its inventor Donald Shell. [7]
- It's also known as the "diminishing increment sort." [8]
- Researchers are still deciding the optimal diminishing increments for large N. [8]
- The last sort of gap size 1 is an insertion sort. [10]

## References:
1. https://www.programiz.com/dsa/bucket-sort
2. https://en.wikipedia.org/wiki/Bogosort
3. https://en.wikipedia.org/wiki/Bucket_sort
4. https://en.wikipedia.org/wiki/Radix
5. https://en.wikipedia.org/wiki/Pigeonhole_sort
6. http://penguin.ewu.edu/cscd300/Topic/AdvSorting/p30-shell.pdf
7. https://dl.acm.org/doi/10.1145/368370.368387
8. Knuth, Donald E. (1997). "Shell's method". The Art of Computer Programming. Volume 3: Sorting and Searching (2nd ed.). Reading, Massachusetts: Addison-Wesley. pp. 83–95. ISBN 978-0-201-89685-5.
9. Sedgewick, Robert. 1996. “Analysis of Shellsort and Related Algorithms.” Fourth Annual European Symposium on Algorithms, September. https://www.cs.princeton.edu/~rs/shell/.
10. Edwards, Rob. 2016. Sorts 5 Shell Sort. https://www.youtube.com/watch?v=ddeLSDsYVp8.
