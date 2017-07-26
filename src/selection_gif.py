import pylab as plt
from random import shuffle

def selectionsort_anim(ls):
    x = range(len(ls))
    for i in range(len(ls) - 1):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls.insert(i, ls[lowest])
        del ls[lowest + 1]
        plt.scatter(x, ls, color='g', marker='.')
        plt.savefig('/cshome/ha10/Pictures/' + '%04d' % i + '.png')
        plt.clf()
        
ls = list(range(300))
shuffle(ls)
selectionsort_anim(ls)
