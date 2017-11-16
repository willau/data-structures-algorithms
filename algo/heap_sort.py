# encoding: utf-8
"""
author: willy au
date: 15 Nov. 2017

Time complexity of heap sort algorithm:
    + Average -> O(n.log(n))
    + Worst   -> O(n.log(n))

Space complexity, we only need one array:
    + O(n)

We use a max heap to sort array here.
Since for a size n, index stems from 0 to n-1.
The parent of node i is given by (i-1)//2.
The children of a node are given by index 2*i+1 and 2*i+2.
"""



def climb(heap, i):
    """ Assume data from 0 to i-1 is a max_heap """
    if i > 0:
        key = heap[i]
        while key > heap[(i-1)//2]:
            heap[i] = heap[(i-1)//2]
            i = (i-1)//2
            if i == 0:
                break
        heap[i] = key


def exchange(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def descent(heap, start, end):
    if start < end:
        i = start
        key = heap[i]
        found = False
        while not found and i <= (end-1)//2:
            i_left, i_right = 2*i+1, 2*i+2
            # edge case when last parent has 1 child
            if i_left == end:
                i_next = i_left
            else:
                if heap[i_left] > heap[i_right]:
                    i_next = i_left
                else:
                    i_next = i_right
            if key >= heap[i_next]:
                found = True
            else:
                heap[i] = heap[i_next]
                i = i_next
        heap[i] = key


def heap_sort(array):
    n = len(array)
    for i in range(1, n):
        climb(array, i)
    for i in range(1, n):
        exchange(array, 0, n-i)
        descent(array, 0, n-i-1)

