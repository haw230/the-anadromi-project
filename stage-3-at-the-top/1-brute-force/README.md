# Fibonacci
Each Fibonacci is equal to the sum of the two before it, starting with 1. The sequence goes 1, 1, 2, 3, 5, 8, 13... For our first stage, let's write a program that takes in the *place* of a **number** in the sequence, called ```n```, in that sequence, and it returns that **number**. Since we're programmers, w'll start counting with 0. When the function is called with a 6, then 13 will be returned.

We need two variables to keep track of the sequence, let's call them ```fn0``` and ```fn1```. At the begining, both will be set to 1. Then we'll iterate a  loop for the number passed in ```n```. With each iteration, we'll set ```fn0``` to ```fn1``` and add the original value of ```fn0``` to ```fn1```. To do this successfully, we'll need a temporary variable.

After that we'll return ```fn0```.

In PseudoCode, it should like:
```python
def fib(n):
    #make two variables to store the sequence
    for i in range(n):
        #make fn0 store fn1
        #add fn0's original value to fn1
    return fn0
```
