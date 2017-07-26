import pylab as plt
from random import shuffle

def bubblesort_anim(a):
 x = range(len(a))
 imgidx = 0
 # bubble sort algorithm
 swapped = True
 while swapped: # until there's no swapping
  swapped = False
  for i in range(len(a)-1):
   if a[i] > a[i+1]:
    a[i+1], a[i] = a[i], a[i+1] # swap
    swapped = True
  plt.plot(x,a,'ro',markersize=6)
  plt.savefig("/cshome/ha10/Pictures/" + '%04d' % imgidx + ".png")
  plt.clf() # figure clear
  imgidx += 1

# running the algorithm
a = list(range(300))
shuffle(a)
bubblesort_anim(a)
