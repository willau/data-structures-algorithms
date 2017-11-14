# encoding: utf-8
"""
author: willy au
date: 13 Nov. 2017
"""

from typing import List


def partition(array: List, l, r) -> int:
    start, end = l, r
    key = array[start]
    l += 1
    while l <= r:
        while array[l] <= key:
            l += 1
            if l > end:
                break
        while array[r] > key:
            r -= 1
        if l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    array[start] = array[r]
    array[r] = key
    return r


def quicksort(array: List, l, r) -> None:
    if l < r:
        i = partition(array, l, r)
        quicksort(array, l, i-1)
        quicksort(array, i+1, r)


