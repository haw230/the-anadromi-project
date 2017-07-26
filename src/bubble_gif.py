import pylab as plt
from random import shuffle

def bubblesort_anim(ls):
    x = range(len(ls))
    imgidx = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                (ls[i + 1], ls[i]) = (a[i], ls[i + 1])
                swapped = True
        plt.plot(x, ls, 'ro', markersize=6)
        plt.savefig('/cshome/ha10/Pictures/' + '%04d' % imgidx + '.png')
        plt.clf()
        imgidx += 1

a = list(range(300))
shuffle(ls)
bubblesort_anim(ls)

			
