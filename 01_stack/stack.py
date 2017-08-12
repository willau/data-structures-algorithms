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
        string = "stack: |"
        for i in range(self.height):
            string += " %d |" % self.array[i]
        for j in range(self.length - self.height):
            string += "   |"
        return string

    def put(self, key):
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


class Link:

    def __init__(self, key, next_link):
        self.key = key
        self.next_link = next_link


class StackLink:

    def __init__(self):
        self.start = None
        self.link = None

    def __repr__(self):
        string = "stack: "
        curr = self.start
        while curr is not None:
            string += "%d --> " %curr.key
            curr = curr.next_link
        string += "null"
        return string

    def put(self, key):
        self.link = Link(key, self.start)
        self.start = self.link
        return self

    def pop(self):
        if self.start is None:
            print("stack is empty")
        else:
            self.link = self.link.next_link
            self.start = self.link
        return self
