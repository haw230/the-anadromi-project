import pylab as plt

const = []
line = []
quad = []
for i in range(50):
    const.append(1)
    line.append(i)
    quad.append(i ** 2)

fig = plt.figure('Time Complexity Graphs')
ax = fig.add_subplot(111)

bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.annotate('Bubble sort (average and worst case), Selection sort(all cases)', ha="center", va="center", xy=(33, 1120), xytext=(30, 1300),
            arrowprops=dict(facecolor='black', shrink=5), bbox=bbox_props
            )

ax.annotate('Linear search', ha="center", va="center", xy=(25, 29), xytext=(25, 305),
            arrowprops=dict(facecolor='black', shrink=5), bbox=bbox_props
            )

ax.annotate('Bubble sort(best case)', ha="center", va="center", xy=(40, 0), xytext=(40, 300),
            arrowprops=dict(facecolor='black', shrink=5), bbox=bbox_props
            )

plt.title('Time Complexity Graphs')

plt.plot(line, const, label = 'Constant O(1)')
plt.plot(line, line, label = 'Linear O(n)')
plt.plot(line, quad, label = 'Quadratic O(n\u00B2)')

plt.xlabel('Input Size of n')
plt.ylabel('Runtime')

plt.legend(loc = 'upper left')

plt.show()

