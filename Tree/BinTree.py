# -*- coding:utf-8 -*-
"""
 Implement the binary tree by using nodes and references. We will define
 a class that has attributes for root,left child and right child.
"""

# Author:Lynn Lau
# Date:2016/10/07
# Language:Python 2.7.11


class BinaryTree:

    def __init__(self, root):
        """ A initial method """
        self.root = root
        self.left = None
        self.right = None

    def insertleft(self, newnode):
        """ insert a left
            Insert a new node to the binary tree as a left subtree
            and put the original left node to the next level.
        """
        if self.left == None:
            self.left = BinaryTree(newnode)
        else:
            temp = BinaryTree(newnode)
            temp.left = self.left
            self.left = temp

    def insertright(self, newnode):
        """insert a right child node
           Insert a new node to the binary tree as a right subtree
           and put the original right node to the next level.
        """
        if self.right == None:
            self.right = BinaryTree(newnode)
        else:
            temp = BinaryTree(newnode)
            temp.right = self.right
            self.right = temp

    def getright(self):
        return self.right

    def getleft(self):
        return self.left

    def getroot(self):
        return self.root

    def setroot(self, newroot):
        self.root = newroot


mytree = BinaryTree('a')
mytree.insertleft('b')
mytree.left.insertright('d')
mytree.insertright('c')
mytree.right.insertleft('e')
mytree.right.insertright('f')
"""
print mytree.getroot()
print mytree.left.getroot()
"""