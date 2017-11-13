# encoding: utf-8
"""
author: willy au
date: 13 Nov. 2017
"""

from typing import List

# TODO: debug edge case [5, 4, 3]
def partition(array: List) -> int:
    key = array[0]
    l, r = 1, len(array)-1
    while l <= r:
        while array[l] <= key:
            l += 1
        while array[r] > key:
            r -= 1
        if l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    array[0], array[r] = array[r], key
    return r

def quicksort(array: List) -> None:
    i = partition(array)
    quicksort(array[:i])
    quicksort(array[i+1:])

