# Binary Search

## Table of Contents
1. [Introduction](#introduction "Why the heck is this important?")
2. [Theory](#theory "Alright, how the heck do I do this?")
3. [PseudoCode](#pseudocode "Let's kinda code this!")
4. [Analysis](#analysis "A bit info")
5. [Extra Resources](#extra-resources "Wanna learn more!")
6. [Coding Task](#coding-task "Coding challenge")
7. [Key Words](#key-words "Important terms")

## Introduction
[*Recursion*](#recursion "Anadromi") is the pinnacle of effective programming. It's complex, it's elegant, and it's effective. The binary search we will be writing today has the time complexity of O(log n) instead of linear search's O(n).
![Alt text](https://github.com/haw230/the-anadromi-project/blob/pictures/linear_vs_log.png)
Even if you don't know how logarithms work, you can still see from the graph that a logarithmic function is much more efficent than a linear one. Binary search relies on dividing and conquering, very similar to the [binary check](https://github.com/haw230/the-anadromi-project/tree/master/stage-2-gaining-speed), which allows it to actually run **faster** than the input size of n. Unlike binary check, we aren't returning a Boolean—we're going to have to return the index.

## Theory
Binary search is all about recursion. It only works on sorted lists, but that's okay—it's fast. As said in the introduction, the search relies on dividing and conquering for its efficency. We don't have to check what logically does not need to be checked. Just like [searching through a phonebook](https://youtu.be/zFenJJtAEzE?t=19m0s), we eliminate half the problem each time using binary search instead of eliminating only a single item with linear search.

When the function takes in a list and the number it's searching for, you can skip to the middle of the list: if your number is greater than that middle number, look at the right side, otherwise, look at the left side (unless that middle number *is* your number in which case just return that).

## PseudoCode
Alright, let's  do some recursion. For recursive functions, we need to be wary of parameters. We'll need ```ls``` and ```num``` as always, because one's the list we're searching and the other is the item we're looking for. But for the recursive function to work, we need two extra parameters: ```low``` and ```high```. These two parameters keep track of what part of the list we currently are looking at and they help us figure out what we return for the index.

```low```, when you call the function the first time is 0 and ```high``` is ```len(ls) - 1```. This is because in your first call, you want start with the entire list. Next, assign ```mid``` to the middle element's index: ```int((low + high) / 2)```. Just like binary check, check if ```ls[mid]``` is ```num```, if so, just give back ```mid```. Otherwise, check whether ```ls[mid]``` is greater or lesser and then call the function accordingly.
```python
def binary_search(ls, num, low, high):
    mid = int((low + high) / 2)
    if(ls[mid] == num):
        return mid
    if(num > ls[mid]):
        return binary_search(ls, num, low, high)
    if(num < ls[mid]):
        return binary_search(ls, num, low, high)
```
Remember for binary check, we had to pass in a sliced version of the list? We can't do the same for binary search otherwise we loose the position of the index. So that's where ```low``` and ```high``` come into place. In our PseudoCode that has come to look suspiciously like real code, calling ```low``` and ```high``` as they are isn't right—we want to shorten the gap between ```low``` and ```high``` with each recursion.

In statement ```if(num > ls[mid]):```, we know that ```num``` has to be on the right side of the list because it's greater than what's just in the middle. So, the lowest index ```num``` can possibly have is going to be one more than the middle number index (since the middle number index is smaller). Or if ```num``` is smaller, we take the left side of the list, so we have all the way from the first element to one less than the middle number index (since the middle number index is larger). We keep doing this until we're only ```low``` and ```high``` finds ```mid```.

But we still have to perform a check to see if the element is *not* in the list ay all. When do we know to stop? Since ```low``` and ```high``` keep track of which part of the list is partitioned, they will slowly zero in on the list until there is one element. If that last element isn't the one we're looking for, then the element we're looking for doesn't exist. When does that happen? When ```low > high```, meaning the algorithm went through the entire list, zeroed in on an item, and still found no reuslts.
## Analysis
With half the problem being cut off each recursion, the time complexity is log n, more efficent than n. This is far faster than linear search.

## Extra Resources
1. [CS50 Lecture covering Binary Search](https://youtu.be/jUyQqLvg8Qw?t=12m)
    * different explanation
2. [Binary Search Animation by Y. Daniel Liang](http://www.cs.armstrong.edu/liang/animation/web/BinarySearch.html)
    * visualization
    
## Coding Task

## Key Words
#### Complex Data Structures
Ints, floats, and strings are basic data structures. Whenever you use one of these values, the Python interpreter just attaches the data to the variable name. However, for complex data structures, the interpreter attaches a reference to the variable instead of the raw value. The reference will point to the list which is made and stored somewhere in the memory.
```python
#Simple Data Type
x = 3
y = x
x += 1 #x is now 4
print(x, y) #4 3

ls1 = [1, 2, 3]
ls2 = ls1
ls1.append(4) #ls1 is now [1, 2, 3, 4]
print(ls1 ls2) #[1, 2, 3, 4] [1, 2, 3, 4]
```
Most of the time the difference between storing references versus storing the actual data is negligible, but here is a good example. The variables ```x``` and ```y``` are completely independant: when ```x``` is changed, ```y``` does not. They're just separate pieces of data. Meanwhile, in the line ```ls2 = ls```, ```ls2``` takes the reference of ```ls1```, which means these two list variables both store a reference to the same list in memory. In the next line, when ```ls1.append(4)``` happens, the list that ```ls1``` references is changed. Since ```ls2``` references it too, it's also changed.

Again, for most of the time, this shouldn't be too concerning. If you wanted two separate lists that don't change each other, just set ```ls2 = [1, 2, 3]``` (creating a completely new list and referencing that) instead of ```ls2 = ls1``` (sets reference to ```ls1```).

Anyway, that explains why we pass in ```ls``` to ```swap()``` without worrying about the function having to return anything—```ls``` will reference the same list we've been trying to sort the whole time so changing that would end up effective.

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

#### Recursion
Recursion is when a function calls it self. Here's a poor implementation of it:
 ```python
 def recurse():
    recurse()
```
Well, that's an infinite loop. Once you run ```recurse()``` it will just keep running itself repeatedly. That's why, when writing recursive functions, we always need a **base case** that stops it and a way to move towards it. Whenever a function calls itself, it creates a **stack** which creates an individual context of the simultaneously executing functions, each with their own variables.

That probably made no sense so here, let's take a look at a recursive function that calculates the factorial of ```num```:
```python
def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)
```
The base case here is when ```num < 2```. There, the function returns 1 and no longer calls itself anymore. When this happens, the other stacks can resolve. What does that even mean? Let's call ```factorial(4)```. ```num``` is set to 4 which is greater than 2 so ```return num * factorial(num - 1)``` will run as ```return 4 * factorial(3)```. Except, what the heck is ```factorial(3)```? The function has to find out so it will call itself with ```num``` as 3. That's greater than two, so ```return 3 * factorial(2)``` runs. Again, what's ```factorial(2)```? Gotta run that and since 2 is not less than 2, ```return 2 * factorial(1)``` runs. Finally, ```num``` is set to 1 which is less than 2, so ```return 1```. Now we have a solid answer without need to call the function again, the stacks resolve. Here's what the process looks like:
```python
factorial(4) #original function call
factorial(4) -> return 4 * factorial(3) #tries to return this but has to run factorial(3)
factorial(3) -> return 3 * factorial(2) #gotta run factorial(2)
factorial(2) -> return 2 * factorial(1) #gotta run factorial(1)
factorial(1) -> return 1 #base case reached
```
Each of the calls are an individual stack. So when the last call finds out that factorial(1) returns 1, it can start solving the other previous calls. ```factorial(2)``` returns ```2 * factorial(1)``` which after the resolution is 2 * 1. ```factorial(3)``` returns ```3 * factorial(2)``` which after the resolution is 3 * 2. ```factorial(4)``` returns ```4 * factorial(3)``` which after the resolution is 4 * 6. Recursion let us do multiple processes in just a few lines of code, allowing for a much more elegant solution than iteration. 

#### Return
This will give back a certain value and end the function process. For example:
```python
def giveThree():
  return 3

three = giveThree()
```
Now the variable ```three``` has been assigned the value of 3. As you can see, this is pretty useless because we could've given ```three``` the value directly instead of making a function return it, but when there is an actually something going on inside the function, returning values becomes much more... *valuable*.
