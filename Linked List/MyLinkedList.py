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
    def __init__(self, initdata):
        self.data = initdata
        self.next_ = None

    # Get the element from the data
    # field of the LinkedList node.
    def getdata(self):
        return self.data

    # Get the next from the link
    # field of the LinkedList node.
    def getnext(self):
        return self.next_

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next_ = newnext

# temp = LinkedNode(93)
# print temp.getdata()

# This class used to init the LinkedList
# and some basic operation.
class LinkedList:

    # Init the LinkedList which is empty
    def __init__(self):
        self.head = None

    # Check whether the LinkedList is empty
    def is_empty(self):
        return self.head is None

    # Add a new node at the beginning of the LinkedList
    def prepend(self, item):
        temp = LinkedNode(item)
        temp.setnext(self.head)
        self.head = temp

    # Add a new node at the end of the LinkedList
    def append(self, item):
        current = self.head
        temp = LinkedNode(item)
        # If the LinkedList is empty we should add the new
        # node at the beginning of the LinkedList.
        if self.head is None:
            self.head = temp
            return
        # If the LinkedList is NOT empty we should scan the whole
        # LinkedList find the last node of the list. Then add the new
        # node at the end of last node.
        while current.next_ is not None:
            current = current.next_
        current.next_ = temp
        temp.next_ = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else :
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())



mylist = LinkedList()
mylist.append(31)
mylist.append(77)
mylist.append(17)
mylist.append(93)
mylist.append(26)
mylist.append(54)
print mylist.size()
print mylist.search(17)