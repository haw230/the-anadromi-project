import pylab
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
  pylab.scatter(x,a,color='g',marker='.')
  pylab.savefig("/cshome/ha10/Pictures/" + '%04d' % j + ".png")
  pylab.clf() # figure clear

# running the algorithm
a = list(range(300)) # initialization of the array
shuffle(a)     # shuffle!
selectionsort_anim(a) # sorting
