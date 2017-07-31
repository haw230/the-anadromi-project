# Recursive Exercise
## What's Recursion?
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

## Binary Check PseudCode
Let's start off with a warm-up exercise: a binary check. It's a watered-down version of the binary search, where you will use recursion to check whether or not an element is indeed inside a list. Here, you only have to return a simple ```True``` or ```False```. Built on dividing and conquering, binary check will be far faster than checking every individual element. The list will be assumed to be sorted already in ascending order.

```python
def binary_check(ls, num):
    #set mid to middle of list
    #check if the middle of the list is equal to num
        return True
    #if num is less than list at mid
        return binary_check(ls[:mid - 1], num)
    #if num is greater than list at mid
        return binary_check(ls[mid + 1:], num)
```
The middle of the list can be easily caculated—it's just ```int(len(ls)/2)```. The ```int()``` is there to convert the float (which includes decimals) to integer (which does not). Doing so would cut off any decimals in case we divide an odd list by 2.

Here's the logic of the algorithm: It starts checking at the middle and if that middle element is greater than the element is less than the element we're searching for, start looking at the smaller half. Otherwise, look at the greater half. Unless of couse, the middle element *is* the on we're looking for, in which case, we ```return True```.

You can see that when we call ```binary_check()``` again, the list is cut down using appendices. ```ls[:mid - 1]``` will only include elements from the beginning to the middle, minus one, while ```ls[mid + 1:]``` will be from the middle to the very end. So, with each call, the list handed into ```binary_check()``` will get smaller (as we're passing in only half of the elements each time). If we were looking for 5 in the list ```[1, 2, 3, 4, 5]```, we know 5 is greater than 3, so what's the point of checking the numbers less than three?

Of course, there's something missing: a ```False``` case. Right after checking if ```num``` is equal to ```ls[mid]```, we need to check ```if(mid == 0)```. If ```mid``` is indeed 0, it means we have one element in that list which means we have not found it.

```python
def binary_check(ls, num):
    #set mid to middle of list
    #check if the middle of the list is equal to num
        return True
    #check if mid is 0
        return False
    #if num is less than list at mid
        return binary_check(ls[:mid - 1], num)
    #if num is greater than list at mid
        return binary_check(ls[mid + 1:], num)
```
Having the ```if(mid == 0)``` **after** the ```if(ls[mid] == num)``` because that last number could very well be the one we're looking for. Alright, that was all the PseudoCode, go [here](https://github.com/haw230/binary-search/tree/binary-check) to implement your solution.
