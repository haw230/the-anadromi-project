# Title

## Table of Contents
1. [Introduction](#introduction "Why the heck is this important?")
2. [Theory](#theory "Alright, how the heck do I do this?")
3. [Pseudocode](#pseudocode "Let's kinda code this!")
4. [Analysis](#analysis "A bit info")
5. [Extra Resources](#extra-resources "Wanna learn more!")
6. [Coding Task](#coding-task "Coding challenge")
7. [Key Words](#key-words "Important terms")

## Introduction
Lets get a [*list*](#list) again, like last time ```[1, 3, 5, 4, 2]```, except it's out of order. Our goal? Sort it. This function will take in that list or a similar one and will output a sorted list in ascending order ```[1, 2, 3, 4, 5]```. We're only going to deal with numbers and we'll be using selection sort to put it in order. Sorting is vital for dealing with data and while programming, there's always lost of data. But [here](https://www.crondose.com/2016/07/sorting-algorithms-important/) is a good article that deals with question "Why are Sorting Algorithms Important?"

## Theory
Selection sort is pretty simple to understand. [*Iterate*](#iterate) through the list and find the lowest number. Move it to the front. Iterate through it again and find the next lowest. Rinse and repeat until the list is sorted.

## Pseudocode
The theory was fairly simple, but the coding will be slightly tougher.
```
selection_sort(ls)
    for every item in ls
        check if it's the smallest
```
Perfect. Done right? Except checking if it's the smallest is harder than it sounds. We're gonna have to iterate through the entire the list a second time, just to find out which one is the smallest. 
```
selection_sort(ls)
    for every item in ls
        lowest_num variable set to zero
        for every item in ls again
            compare lowest_num with the item, if the item is smaller, that's actually the lowest value
                set lowest_num to that item
        by now, the lowest has been found, so move that to the front
```
Man, that's a lot of steps **and** it's still not done. ```ls.insert(0, item_name)```
## Analysis

## Extra Resources
[Why are Sorting Algorithms Important?](https://www.crondose.com/2016/07/sorting-algorithms-important/)

## Coding Task

## Key Words
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
