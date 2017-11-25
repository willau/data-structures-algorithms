# encoding: utf-8
"""
author: willy au
date: 14 Nov. 2017
"""

from typing import List


def selection_sort(array: List):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if array[j] <= array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


def insertion_sort(array: List):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i
        while key < array[j-1] and j > 0:
            array[j] = array[j-1]
            j = j-1
        array[j] = key


def buble_sort(array: List):

    def switch(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    for __ in range(n):
        for i in range(n-1):
            if array[i] >= array[i+1]:
                switch(i, i+1)

