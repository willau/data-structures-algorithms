# encoding: utf-8
"""
author: willy au
date: 12 August 2017
"""

class StackArray:

    def __init__(self, n=10):
        assert n > 0
        self.length = n
        self.array = list(-1 for _ in range(n))
        self.height = 0

    def __repr__(self):
        string = "|"
        for i in range(self.height):
            string += " %d |" % self.array[i]
        return string

    def append(self, key):
        if self.height < self.length:
            self.array[self.height] = key
            self.height += 1
        else:
            print("stack is full")
        return self

    def pop(self):
        if self.height == 0:
            print("stack is empty")
        else:
            self.array[self.height - 1] = -1
            self.height -= 1
        return self


if __name__ == "__main__":
    print("stack implementation with array")
