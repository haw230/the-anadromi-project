# Recursive Fibonacci
The recursive vesion should be simpler to write than the iterative, but likely much harder to visualize. As always, the function will take in ```n``` and return what number of the Fibonacci sequence is at ```n```. The way our recursive Fibonacci function will work is that the function will call itself with the two numbers before ```n``` (so when it calls itself, the parameters will be ```n - 1``` and ```n - 2```). Then the numbers before those numbers will call their two preceding numbers.

[![tree](https://github.com/haw230/the-anadromi-project/blob/pictures/fib_tree.png)](http://www.dartmouth.edu/~matc/DiscreteMath/IV.1.pdf)

As shown by the tree, eventually the numbers will decompose to 1s, which trickles upwards and reconstructs each number of the sequence, adding up to the answer. Our pseudocode would look something like this:
``` python
def fib(n):
    #basecase
        return 1
    return #recursive call
```
Go [here](https://github.com/haw230/recursive-fibonacci) for your coding task.

When you're done and the tests ran successfully, try uncommenting the last test (located in ```tests``` folder<```test_main.py```>the class```TestCases(Object)```>the method ```def tests(self)```):

![c9](https://github.com/haw230/the-anadromi-project/blob/pictures/uncomment.png)

Run it again and see what happens! (Or, to be price, what doesn't happen)
