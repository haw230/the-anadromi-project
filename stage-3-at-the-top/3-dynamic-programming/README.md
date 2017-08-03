# Dynamic Programming
When you ran ```fib(60)```, that must've taken a while. The larger ```n``` is, the worse the time that the function runs. In the form of a binary tree, it will run **exponential** time. It's pretty slow, so we're going to need to write another function that runs faster. With memoization, a subset of dynamic programming, we can do just that.

But first let's look at *why* the recursive Fibonacci is so slow.
 ```python
Let's call fib() with 5
Execution Stack: fib(5)
#then it will call
Execution Stack: fib(4), fib(3)
#heading down the left side of the tree, fib(4) will run first
Execution Stack: fib(3), fib(2), fib(3)
#travelling down fib(3)
Execution Stack: fib(2), fib(1), fib(2), fib(3)
```
The function is far from finished, but as you can see from just that, ```fib()``` will call itself with parameters it had processed previously. After ```fib(3)``` runs, there's another ```fib(3)``` waiting in the stack. It would be so much faster to store the values ```fib(3)``` and look it up instead of going through the tree once more. This is how memoization works—by storing branches inside a dictionary and accessing branches that have ran before.

To do this, let's declare a ```memo``` dictionary to store the branches and as always, ```fib()``` will take an ```n```. Remember that a dictionary is a complex data type, meaning that no matter which call of ```fib()``` we are on, the same ```memo``` dictionary can be accessed or edited. For the most part, ```fib(n)``` will look like its recursive counterpart:
```python
memo = {}
def fib(n):
    if n < 2: #exact same base case
        return 1
```
Next, we'll need to store the branches inside of ```memo```. Each branch of ```n``` is a different call of ```fib()```, and each branch is contructed from calling ```fib(n - 1)``` and ```fib(n - 2)```. So, instead of returning those two calls like the recursive implementation, we will store them inside the dictionary. A dictionary, unlike an array, is accessed by keys. These keys can be numbers, so we'll just set ```memo```'s ```n``` property to ```fib(n - 1) + fib(n - 2)``` (you can set a key to a value like this ```dict[key] = value```). Then, just return whatever value you've just stored.
```python
memo = {}
def fib(n):
    if n < 2: #exact same base case
        return 1
    memo set to previous two brances #don't actually use the key word set, it's still PseudoCode, just with color
    return value of memo with n key #don't actually use the key word with
```
Okay, so we've got the dictionary storing the branches, but we haven't used them yet. We need to check if the branch has been saved into the dictionary before. Just use an ```if(n in memo):``` and we're good. So if the key has been stored before, what do we do? Just return the value of ```memo``` with that particular key. And here's our final PseudoCode:
```python
memo = {}
def fib(n):
    if n < 2: #exact same base case
        return 1
    if n in memo:
        return n at memo
    memo set to previous two brances #don't actually use the key word set, it's still PseudoCode, just with color
    return value of memo with n key #don't actually use the key word with
```
Let's run this PseudoCode in our heads:
 ```python
Calling fib() with 5
Execution Stack: fib(5)
#then it will call
Execution Stack: fib(4), fib(3)
#heading down the left side of the tree, fib(4) will run first
Execution Stack: fib(3), fib(2), fib(3)
#travelling down fib(3)
Execution Stack: fib(2), fib(1), fib(2), fib(3)
```
Go [here](https://github.com/haw230/dynamic-fibonacci) for the coding task.
