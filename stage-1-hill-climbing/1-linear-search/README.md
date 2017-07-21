# Linear Search

## Introduction

Suppose I had a collection of numbers, which we'll call a [*list*](list "collection of numbers"), how would I find a specific [*element*](element "just an item") in that list? Let's take the list ```[1, 2, 3, 4 ,5]``` and let's say I wanted to find the [*index*](index "position in list") of the number 3. The way the linear search algorithm works is that it will compare the number we are looking for with every element in the list, starting from the beginning. First, it would compare 3 with 1. They're not equal, so we move on to 2. 3 doesn't equal 2, so we move on again. Now we have reached 3 and 3—they match and we [*return*](return "give back") the index.




## Key words
#### List
A list is just a collection of numbers. This collection can contain however many numbers and each number can be of any value (we shouldn't have to worry about going over the maximum size of a list or the maximum value of a number in the scope of this lesson). For example ```[1, 2, 3, 4 ,5]``` is a list and ```[10, 4, 5, 9.5, 4, 5.4]``` is another. Heck, it can even include strings (text). ```[1, 2, 'three']``` is a totally valid list. 

In some other languages, it is referred to as an *array*.

#### Element
An item inside a list. In the list ```[1, 2, 3]``` 1, 2, and 3 are all elements.

#### Index
The index is the *numerical position* of an element inside a list. Programmers count starting from zero (because it's slightly more efficent), so each number is one less than what we would normally call it in real life. In ```[1, 2, 3]```, 1 may seem like the first element, but it is actually the zeroth. 2 would be the first and 3 is the second. So to match the index with each element, it would look like 0:1, 1:2, and 2:3.

#### Return
This will give back a certain value and end the function process. For example:
```python
def giveThree():
  return 3

three = giveThree()
```
Now the variable ```three``` has been assigned the value of 3. As you can see, this is pretty useless because we could've given ```three``` the value directly instead of making a function return it, but when there is an actually something going on inside the function, returning values becomes much more... *valuable*.






















Go [here](https://github.com/haw230/linear-search/ "Linear Search") to complete the first project!
