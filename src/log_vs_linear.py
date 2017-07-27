import pylab as plt
import math

line = []
log = []

for i in range(1, 50):
    line.append(i)
    log.append(math.log10(i))

plt.title("Linear vs Logarithmic Graph")

plt.plot(line, line, label = 'Linear Search O(n)')
plt.plot(line, log, label = 'Binary Search O(log n)')

plt.xlabel('Input Size of n')
plt.ylabel('Runtime')

plt.legend(loc = 'upper left')

plt.show()
