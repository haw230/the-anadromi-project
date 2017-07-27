# Time Complexity
Time complexity measures the running time of an algorithm when given an input size. This measure isn't meant to be accurate—it just finds a rough idea of how efficent the algorithm is. The most common way of representing this is through the *big-O* notation (the name isn't creative, it's just a capital O function). Typically this notation describes the upper bound, or otherwise known as the worst-case runtime scenario. There are other notations such as *big-Ω notation* which describes the lower bound (best possible time), but big-O is most common and remember that the others only describe different bounds. We'll take some common representations of time complexity and examine them.

## O(1)
```O(1)``` describes a *constant* function. No matter what you input, the number of steps it takes will be simply 1. This occurs when there are no loops at all.
```python
def some_func(ls):
    return ls
```
This function isn't very useful, but it is efficent. Whether ```ls``` contains 3 items or 3000, the function will always run in one step.

## O(n)
```O(n)``` is a *linear* function. Unlike ```O(1)```, the time will grow as the sample size of ```n``` increases, but it is still very efficent. To have an algorithm run at ```O(n)``` is goal for all. This occurs when there is a loop.
```python
def add_up(ls):
  for i in ls:
      i + 1
  return ls
```
Depending how large ```ls``` is, the time will grow accordingly. But notice there is a ```return ls```, so technically it should be ```O(n + 1)```, but that 1 matters so little in the running time we simply drop it.

## O(n²)
```O(n²)``` is a ```quadratic``` function and it much, much less efficent at ```O(n)```. The ```n²``` will grow far faster than ```n```, resulting in a very inefficent run time depending on the input size ```n```. This complexity occurs when there are is a nested loop (a loop inside a loop).
```python
def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i, len(ls)):
            if ls[lowest] > ls[j]:
                lowest = j
        ls.insert(i, ls[lowest])
        del ls[lowest + 1]
    return ls
```
Well, this must look familiar. Selection sort had a very inefficent time complexity because it loops over the input twice. It goes over the list to find the smallest element, move it to the its designated spot, and has to do this for **each** element of the list. For a list of ```[2, 1, 3]```, selection must go over the list to find the 1, move it at the front, then again to find the 2 and moves it, then again for 3 and move that. We might know that after inserting the 1 in its proper place, the list is already sorted, but the program doesn't know that and will continue running and checking.

## Conclusion
Well, those were some important measures of algorithm efficency. There's more to cover in part two,  Here's the complexity of the algorithms we've seen so far:
![alt text](https://github.com/haw230/the-anadromi-project/blob/pictures/time_complexity_graph.png "Time Complexity Graph")

