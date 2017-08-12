# encoding: utf-8
"""
author: willy au
date: 12 August 2018
"""


class QueueArray:

    def __init__(self, n=10):
        self.start = 0
        self.end = 0
        self.array = list(-1 for _ in range(n))
        self.n = n

    def __repr__(self):
        string = "queue: |"
        for e in self.array:
            string += " %s |" % e if e!= -1 else "   |"
        return string

    def put(self, key):
        assert type(key) == int
        sta = self.start
        end = self.end
        diff = sta - end
        if sta != end and diff % self.n == 0:
            print("queue is full")
        else:
            self.array[end % self.n] = key
            self.end += 1
        return self

    def pop(self):
        if self.start == self.end:
            print("queue is empty")
        else:
            self.array[self.start % self.n] = -1
            self.start += 1
        return self


class Link():

    def __init__(self, key, next_link):
        self.key = key
        self.next_link = next_link


class QueueLink:

    def __init__(self):
        return None

    def __repr__(self):
        return ""

    def put(self):
        return None

    def pop(self):
        return None

