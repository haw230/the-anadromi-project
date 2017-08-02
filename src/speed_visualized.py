import pylab as plt
import time
import random
import sys
sys.setrecursionlimit(15000000)

#bubble sort start
def bubble_sort(ls):
    sort_done = False
    while (not sort_done):
        sort_done = True
        for i in range(len(ls) - 1):
            if (ls[i] > ls[i + 1]):
                swap(ls, i)
                sort_done = False
    return ls


def swap(ls, i):
    temp = ls[i]
    ls[i] = ls[i + 1]
    ls[i + 1] = temp
#bubble sort end

#selection sort start
def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i, len(ls)):
            if ls[lowest] > ls[j]:
                lowest = j
        ls.insert(i, ls.pop(lowest))
    return ls
#selection sort end

#merge sort start
def merge_sort(ls):
    if(len(ls) < 2):
        return ls
    mid = int(len(ls) / 2)
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])
    return merge(left, right)

def merge(l, r):
    result = []
    while(len(l) > 0 and len(r) > 0):
        if r[0] < l[0]:
            result.append(r.pop(0))
        else:
            result.append(l.pop(0))
    result.extend(l + r)
    return result
#merge sort end

#quicksort start
def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right
#quicksort end

#linear search start
def linear_search(ls, num):
    for i in range(len(ls)):
        if ls[i] == num:
            return i
    return -1
#linear search end

#binary search start
def binary_search(ls, num, low, high):
    if(low > high):
        return -1
    mid = int((low + high) / 2)
    if(ls[mid] == num):
        return mid
    if(num > ls[mid]):
        return binary_search(ls, num, mid + 1, high)
    if(num < ls[mid]):
        return binary_search(ls, num, low, mid - 1)
#binary search end

def time_it_sort(func, param):
    start = time.clock()
    func(param)
    return time.clock() - start

def time_it_quick(func, ls, low, high):
    start = time.clock()
    func(ls, low, high)
    return time.clock() - start

def time_it_search(func, param, num=0, low=0, high=0):
    start = time.clock()
    if(high != 0):
        func(param,  num, low, high)
    else:
        func(param, num)
    return time.clock() - start

def main():
    ls_size = [x for x in range(0, 31000, 1000)]

    #sort graphs
    time_bubble = []
    time_selection = []
    time_merge = []
    time_quick= []
    
    for i in ls_size:
        print(i/1000)
        ls = list(range(0, i))
        random.shuffle(ls)
        
        time_bubble.append(time_it_sort(bubble_sort, ls))
        time_selection.append(time_it_sort(selection_sort, ls))
        time_merge.append(time_it_sort(merge_sort, ls))
        time_quick.append(time_it_quick(quicksort, ls, 0, len(ls) - 1))
      
    plt.plot(ls_size, time_bubble, marker='o', color='r', label='Bubble Sort')
    plt.plot(ls_size, time_selection, marker='o', color='b', label='Selection Sort')
    plt.plot(ls_size, time_merge, marker='o', color='g', label='Merge Sort')
    plt.plot(ls_size, time_quick, marker='o', color='y', label='Quicksort')
    #sort graphs end
    '''
    #search graphs
    time_linear = []
    time_binary = []

    for i in ls_size:
        print(i/1000)
        ls = list(range(0, i))

        time_linear.append(time_it_search(linear_search, ls, num=random.choice(ls)))
        time_binary.append(time_it_search(binary_search, ls, num=random.choice(ls), low=0, high=len(ls)-1))

    plt.scatter(ls_size, time_linear, marker='o', color='b', label='Linear Search')
    plt.plot(ls_size, time_binary, marker='o', color='g', label='Binary Search')
    #search graphs end
    '''

    plt.title('Merge Sort vs Quicksort')
    plt.xlabel('List Size', fontsize=18)
    plt.ylabel('Time (s)', fontsize=18)    
    plt.legend(loc = 'upper left', prop={'size': 18})
    plt.show()
    
    
main()
