# Linear Search

## Introduction

Suppose I had a collection of numbers, which we'll call a [*list*](list "collection of numbers"), how would I find a specific [*element*](element "just an item") in that list? Let's take the list ```[1, 2, 3, 4 ,5]``` and let's say I wanted to find the [*index*](index "position in list") of the number 3. The way the linear search algorithm works is that it will compare the number we are looking for with every element in the list, starting from the beginning. First, it would compare 3 with 1. They're not equal, so we move on to 2. 3 doesn't equal 2, so we move on again. Now we have reached 3 and 3—they match and we [*return*](return "give back") the index. If by the end, there has been no matches, just return -1. The problem is solved!

## Pseudocode
Of course, we have to code it. Here, I'll present the pseudocode and theory necessary to successfully implement a linear search. 
```
linear_search(ls, num)
    index variable set to 0
    for every item in ls
```
We need an ```index``` variable in order to keep track of where we are. This variable should [*increment*](#increment "Add consistenly by the number") by 1 as we pass through the list. This index is what the function will return once we find the number. 

Next is the for loop. We need this is [*iterate*](iterate "go over each") through the list that is given. It allows the function to check every element. Each will be compared to num, which is the number we are looking for
```
linear_search(ls, num)
    index variable set to 0
    for every item in ls
        if this item equals num
            give back the index and stop the loop
```
Luckily for us, ```return index``` will give back the index AND stops the loop at the same (once ```return``` statements run, the function is exited). The algorithm is almost complete—we just need to return -1 if there is no match at all.

```
linear_search(ls, num)
    index variable set to 0
    for every item in ls
        if this item equals num
            give back the index and stop the loop
    give back -1
```
Here, notice that the ```give back -1``` is not included in the loop (notice the indentation levels). If it was in the loop, the loop would end after one iteration and just ```return -1```. By having it outside of loop, we are certain it will run **after** the entire list has been iterated over already.

## Analysis

## Resources
<a href="https://youtu.be/jUyQqLvg8Qw?t=8m45s" target="_blank">Harvard's CS50 Lecture including Linear Search</a>

## Key words
#### Element
An item inside a list. In the list ```[1, 2, 3]``` 1, 2, and 3 are all elements.

#### List
A list is just a collection of numbers. This collection can contain however many numbers and each number can be of any value (we shouldn't have to worry about going over the maximum size of a list or the maximum value of a number in the scope of this lesson). For example ```[1, 2, 3, 4 ,5]``` is a list and ```[10, 4, 5, 9.5, 4, 5.4]``` is another. Heck, it can even include strings (text). ```[1, 2, 'three']``` is a totally valid list. 

In some other languages, it is referred to as an *array*.

#### Increment
Adding a fixed number consistently. Opposite is decrement. Unlike C-based languages, Python does not suppose the ```++``` short hand to have variables increment by 1, so ```+= 1``` is used instead.

#### Index
The index is the *numerical position* of an element inside a list. Programmers count starting from zero (because it's slightly more efficent), so each number is one less than what we would normally call it in real life. In ```[1, 2, 3]```, 1 may seem like the first element, but it is actually the zeroth. 2 would be the first and 3 is the second. So to match the index with each element, it would look like 0:1, 1:2, and 2:3.

#### Iterate
Repeating a process for each element until a condition has been reached in which case it is stopped. For linear search, the process will be comparing the element with the number we are trying to locate.

#### Return
This will give back a certain value and end the function process. For example:
```python
def giveThree():
  return 3

three = giveThree()
```
Now the variable ```three``` has been assigned the value of 3. As you can see, this is pretty useless because we could've given ```three``` the value directly instead of making a function return it, but when there is an actually something going on inside the function, returning values becomes much more... *valuable*.






















Go [here](https://github.com/haw230/linear-search/ "Linear Search") to complete the first project!
