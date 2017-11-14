# encoding: utf-8
"""
author: willy au
date: 14 Nov. 2017
"""

from typing import List


def quick_sort(array: List, l, r) -> None:
    if l < r:
        i = partition(array, l, r)
        quick_sort(array, l, i-1)
        quick_sort(array, i+1, r)


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
