# Title

## Table of Contents
1. [Introduction](#introduction "Why the heck is this important?")
2. [Theory](#theory "Alright, how the heck do I do this?")
3. [PseudoCode](#pseudocode "Let's kinda code this!")
4. [Analysis](#analysis "A bit info")
5. [Extra Resources](#extra-resources "Wanna learn more!")
6. [Coding Task](#coding-task "Coding challenge")
7. [Key Words](#key-words "Important terms")

## Introduction

## Theory

## PseudoCode

## Analysis

## Extra Resources

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

#### Return
This will give back a certain value and end the function process. For example:
```python
def giveThree():
  return 3

three = giveThree()
```
Now the variable ```three``` has been assigned the value of 3. As you can see, this is pretty useless because we could've given ```three``` the value directly instead of making a function return it, but when there is an actually something going on inside the function, returning values becomes much more... *valuable*.
