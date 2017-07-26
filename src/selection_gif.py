import pylab as plt
from random import shuffle

def selectionsort_anim(a):
 x = range(len(a)) 
 for j in range(len(a)-1):
  iMin = j
  for i in range(j+1,len(a)):
   if a[i] < a[iMin]: # find the smallest value
    iMin = i
  if iMin != j: # place the value into its proper location
   a[iMin], a[j] = a[j], a[iMin]
  # plotting
  plt.scatter(x,a,color='g',marker='.')
  plt.savefig("/cshome/ha10/Pictures/" + '%04d' % j + ".png")
  plt.clf() # figure clear

# running the algorithm
a = list(range(300)) # initialization of the array
shuffle(a)     # shuffle!
selectionsort_anim(a) # sorting
