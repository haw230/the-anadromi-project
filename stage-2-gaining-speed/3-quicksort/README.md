# Quicksort
Quicksort is the most modern, most used sorting algorithm. It divides and conquers but different way than merge sort. Quick sort picks a pivot (any element), shifts the list (partitioning) until the left is less and the right is greater than or equal to the pivot. The left side is sorted and then a new pivot is chosen and repeated until the entire list is done. Compared to merge sort (which as you saw previously, [blew bubble sort and selection sort completely away](https://github.com/haw230/the-anadromi-project/blob/pictures/s_vs_b_vs_m.png)), quicksort is slightly faster:
![graph](https://github.com/haw230/the-anadromi-project/blob/pictures/merge_vs_quick.png)

But with a bad pivot, it will be slower than selection sort:
![graph](https://github.com/haw230/the-anadromi-project/blob/pictures/quicksort.png)
