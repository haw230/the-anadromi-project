import pylab as plt
import time
import random

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

def time_it(func, param):
    start = time.clock()
    func(param)
    return time.clock() - start

def main():
    time_bubble = []
    time_selection = []
    time_merge = []

    ls_size = [x for x in range(0, 21000, 1000)]
    for i in ls_size:
        print(i/1000)
        ls = list(range(0, i))
        random.shuffle(ls)
        
        time_bubble.append(time_it(bubble_sort, ls))
        time_selection.append(time_it(selection_sort, ls))
        time_merge.append(time_it(merge_sort, ls))
        
    plt.plot(ls_size, time_bubble, marker='o', color='r', label = 'Bubble Sort')
    plt.plot(ls_size, time_selection, marker='o', color='b', label='Selection Sort')
    plt.plot(ls_size, time_merge, marker='o', color='g', label='Merge Sort')
    plt.xlabel('List Size', fontsize=18)
    plt.ylabel('Time (s)', fontsize=18)    
    plt.legend(loc = 'upper left')
    plt.show()
    
main()
