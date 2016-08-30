# -*- coding:utf-8 -*-

# Data Structure and Algorithm with Python, DSA
# Author:Lynn Lau
# Language: Python 2.7.11
# Date: 2016/08/30
# Topic: Basic Linked List


# This class is used to define some basic properties
# of the node in LinkedList.
class LinkedNode:

    # Init the node
    def __init__(self, elem, next_):
        self.elem = elem
        self.next_ = next_
        self.next_ = None

    # Get the element from the data
    # field of the LinkedList node.
    def getdata(self):
        return self.elem

    # Get the next from the link
    # field of the LinkedList node.
    def getnext(self):
        return self.next_

    def setdata(self, newdelem):
        self.elem = newdelem

    def setnext(self, newnext):
        self.next_ = newnext


# This class used to init the LinkedList and
# some basic operation.
class LinkedList:

    # Init the LinkedList which is empty
    def __init__(self):
        self._head = None

    # Check whether the LinkedList is empty
    def is_empty(self):
        return self._head is None

    # Add a new node at the beginning of the LinkedList
    def prepend(self, elem):
        self._head = LinkedNode(elem, self._head)

    # Add a new node at the end of the LinkedList
    def append(self, elem):
        # If the LinkedList is empty we should add the new
        # node at the beginning of the LinkedList.
        if self._head is None:
            self._head = LinkedNode(elem)
            return
        # If the LinkedList is NOT empty we should scan the whole
        # LinkedList find the last node of the list. Then add the new
        # node at the end of last node.
        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = LinkedNode(elem)

