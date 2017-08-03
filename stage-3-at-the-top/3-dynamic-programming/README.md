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
As you can see, ```fib()``` calls itself with parameters that it had down before. It would be so much faster to store the values ```fib(3)``` and ```fib(2)``` and look it up instead of running them again. This is how memoization works—by storing branches inside a dictionary and accessing branches that have ran before.

To do this, let's declare a ```memo``` dictionary to store the branches and as always, ```fib()``` will take an ```n```. For the most part, ```fib(n)``` will look like its recursive counterpart:
```python
memo = {}
def fib(n):
    if n < 2: #exact same base case
        return 1
```
Next, we'll need to store the branches inside of ```memo```. Each branch is a different call of ```fib()```, 

Go [here](https://github.com/haw230/dynamic-fibonacci) for the coding task.
