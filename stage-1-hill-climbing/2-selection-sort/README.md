# Selection Sort

## Table of Contents
1. [Introduction](#introduction "Why the heck is this important?")
2. [Theory](#theory "Alright, how the heck do I do this?")
3. [PseudoCode](#pseudocode "Let's kinda code this!")
4. [Analysis](#analysis "A bit info")
5. [Extra Resources](#extra-resources "Wanna learn more!")
6. [Coding Task](#coding-task "Coding challenge")
7. [Key Words](#key-words "Important terms")

## Introduction
Lets get a [*list*](#list) again: ```[1, 3, 5, 4, 2]```. Our goal? Sort it. This function will take in that list or a similar one and will output a sorted list in ascending order ```[1, 2, 3, 4, 5]```. We're only going to deal with numbers and we'll be using selection sort to put it in order. Sorting is vital for dealing with data and while programming, there's always lost of data. But [here](https://www.crondose.com/2016/07/sorting-algorithms-important/) is a good explanation of the importance of sorting algorithms. Even if they aren't that important, they're still great for coding practice.

## Theory
Selection sort is pretty simple to understand. [*Iterate*](#iterate) through the list and find the lowest number. Move it to the front. 
![Alt Text](https://github.com/haw230/the-anadromi-project/blob/pictures/selection_sort_animation.gif)
Iterate through it again and find the next lowest. Rinse and repeat until the list is sorted.

## PseudoCode
The theory was fairly simple, but the coding will be slightly tougher.
```
selection_sort(ls)
    for every item in ls
        check if it's the smallest
        move that to the front
```
Perfect. Done right? One problem: checking for the smallest is harder than it seems. We're gonna have to iterate through the entire the list just to find out which element is the smallest. But let's change the first for loop to ```for i in range(len(ls))```. ```range()``` makes a list counting by ones from 0 to the length of ```ls```. If ```ls``` has 3 items, ```range()``` will make ```[0, 1, 2]```. So with each iteration, ```i``` will store the [*index*](#index) of where to insert the lowest value. ```i``` would refer to ```0``` in the first iteration, which is where the lowest element will go and then ```i``` would refer to ```1``` would refer to ```1``` in the second iteration.

```
selection_sort(ls)
    for i in range(len(ls))
        index_of_lowest variable set to i
        for j in range(len(ls))
            compare ls at j with the ls at the index_of_lowest, if the ls at j is smaller
                set index_of_lowest to j
        by now, index_of_lowest has the lowest index, so move that to i
```
Man, that's a lot of steps, but we're not quite done yet. We have to [*insert*](insert) it. With ```ls.insert(i, item)```, we can do just that. It's not as easy as simply inserting it because if we just blindly insert the item in there, we would have duplicates in the list. We also need to delete the item that we inserted. Since we know that ```insert()``` pushes everything back by 1, the index will just be ```index_of_lowest + 1```, due to the insertion.

Alright, here's our final PseudoCode.
```
selection_sort(ls)
    for i in range(len(ls))
        index_of_lowest variable set to i
        for j in range(i, len(ls))
            compare ls at j with the ls at the index_of_lowest, if the ls at j is smaller
                set index_of_lowest to j
        by now, index_of_lowest has the lowest index, so insert that to i
        delete the item at index_of_lowest + 1
    give back the list
```
## Analysis
Selection is a pretty inefficent sort. For larger lists, you're going to be checking over everything many, many times. For our small data sets, this won't really make a difference, but once we get over, let's say, 1000 items, the speed will be noticeably slower than the more efficent algorithm.

## Extra Resources
1. [Why are Sorting Algorithms Important?](https://www.crondose.com/2016/07/sorting-algorithms-important/)
    * Explains the importance of sorting algorithms...we're going to be writing a lot of these!
2. [Harvard's CS 50 Lecture covering Selection sort](https://youtu.be/jUyQqLvg8Qw?t=27m50s)
    * An explanation of the algorithm
3. [Visualization by VisuAlgo](https://visualgo.net/en/sorting)
    * A visualization with PseudoCode. Remember to click Selection Sort at the top, the default is Bubble Sort.

## Coding Task
Go [here](https://github.com/haw230/selection-sort) to complete your coding task!

## Key Words
#### Element
An item inside a list. In the list ```[1, 2, 3]``` 1, 2, and 3 are all elements.

#### Increment
Adding a fixed number consistently. Opposite is decrement. Unlike C-based languages, Python does not suppose the ```++``` short hand to have variables increment by 1, so ```+= 1``` is used instead.

#### Index
The index is the *numerical position* of an element inside a list. This is important for tracking the location of a specific element. The numbering system is slightly convoluted since, programmers count starting from zero (because it's slightly more efficent), so each number is one less than what we would normally call it in real life. In ```[1, 2, 3]```, 1 may seem like the first element, but it is actually the zeroth. 2 would be the first and 3 is the second. So to match the index with each element, it would look like 0:1, 1:2, and 2:3.

#### Insert
This isn't so much a definition as it is an explanation of the ```insert()``` function. It takes the an index and an element, and it inserts the entered element at the position of the entered index pushes everything back.
```python
ls = [1, 2, 3]
ls.insert(0, 0)
print(ls) #will print [0, 1, 2, 3]
```
Be careful you don't set ```ls``` to ```ls.insert(0, 0)```. That would change ```ls``` to ```None```.

#### Iterate
Repeating a process for each element until a condition has been reached in which case it is stopped. For linear search, the process will be comparing the element with the number we are trying to locate.

#### List
A list is just a collection of numbers. This collection can contain however many numbers and each number can be of any value (we shouldn't have to worry about going over the maximum size of a list or the maximum value of a number in the scope of this lesson). For example ```[1, 2, 3, 4 ,5]``` is a list and ```[10, 4, 5, 9.5, 4, 5.4]``` is another. Heck, it can even include strings (text). ```[1, 2, 'three']``` is a totally valid list. 

In some other languages, it is referred to as an *array*.

#### Return
This will give back a certain value and end the function process. For example:
```python
def giveThree():
  return 3

three = giveThree()
```
Now the variable ```three``` has been assigned the value of 3. As you can see, this is pretty useless because we could've given ```three``` the value directly instead of making a function return it, but when there is an actually something going on inside the function, returning values becomes much more... *valuable*.
