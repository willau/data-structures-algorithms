# encoding: utf-8
"""
author: willy au
date: 16 Nov. 2017

Binary search tree <-> BST
Time complexity of BST sort algorithm:
    + Average -> O(n.log(n))
    + Worst   -> O(n^2)

Space complexity, tree and array each takes O(n)
    + O(n)

Bug encountered:
    + self.root = None, does not work
        + Cause: reference to self.root is lost
        + Consequence: insert_at_node replace None by None
        + Solution:
            + use a function 'isnull()' to create null node
            + use the fact that class can be referenced
    + remember to use 'None' with cautious next time
"""


def bst_sort(array):
    bstree = BSTree()
    for e in array:
        bstree.insert(e)
    array = list()
    infix_traversal(bstree.root, array)
    return array


def infix_traversal(node, array):
    if node.left is not None:
        infix_traversal(node.left, array)
    array.append(node.data)
    if node.right is not None:
        infix_traversal(node.right, array)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def isnull(self):
        return (self.data is None)


class BSTree:
    def __init__(self):
        self.root = Node()
        self.array = list()

    def insert_at_node(self, node, data):
        if node.isnull():
            node.data = data
        else:
            if data >= node.data:
                if node.right is None:
                    node.right = Node()
                self.insert_at_node(node.right, data)
            else:
                if node.left is None:
                    node.left = Node()
                self.insert_at_node(node.left, data)

    def insert(self, data):
        self.insert_at_node(self.root, data)

