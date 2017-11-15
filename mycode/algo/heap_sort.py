# encoding: utf-8
"""
author: willy au
date: 15 Nov. 2017
"""

# Avrge complexity: O(n.logn)
# Worst complexity: O(n^2)

class MinHeap:

    def __init__(self, n=10):
        self.array_length = n+1
        self.array = list([-1]*self.array_length)
        self.last = 1

    def insert_from_bottom(self, data):
        A = self.array
        if self.last == 1:
            A[1] = data
            self.last += 1
        else:
            i = self.last
            while data < A[i//2]:
                A[i] = A[i//2]
                i = i//2
                if i == 1:
                    break
            A[i] = data
            self.last += 1

    def exchange(self, i, j):
        A = self.array
        A[i], A[j] = A[j], A[i]

    def insert_list(self, integers):
        n_int = len(integers)
        if len(integers) <= len(self.array):
            for i in integers:
                self.insert_from_bottom(i)
        else:
            raise ValueError('Internal array too short')


    # TODO: debug edge case of lonely child
    def switch_descent(self):
        A = self.array
        if self.last > 1:
            if self.last == 3:
                if A[1] > A[2]:
                    self.exchange(1, 2)
            else:
                self.exchange(1, self.last - 1)
                j = 1
                key = A[1]
                while key > min(A[2*j], A[2*j+1]):
                    if A[2*j] < A[2*j+1]:
                        j_min = 2*j
                    else:
                        j_min = 2*j+1
                    A[j] = A[j_min]
                    j = j_min
                    if 2*j+1 >= self.last:
                        break
                A[j] = key
            self.last -= 1


#if __name__ == "__main__":

