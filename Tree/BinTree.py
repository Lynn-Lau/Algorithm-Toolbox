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
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, newnode):
        """ insert a left
            Insert a new node to the binary tree as a left subtree
            and put the original left node to the next level.
        """
        if self.leftchild == None:
            self.leftchild = BinaryTree(newnode)
        else:
            temp = BinaryTree(newnode)
            temp.leftchild = self.leftchild
            self.leftchild = temp

    def insertright(self, newnode):
        """insert a right child node
           Insert a new node to the binary tree as a right subtree
           and put the original right node to the next level.
        """
        if self.rightchild == None:
            self.rightchild = BinaryTree(newnode)
        else:
            temp = BinaryTree(newnode)
            temp.rightchild = self.rightchild
            self.rightchild = temp

    # This code blocks will return the rightchild, leftchild and root of the 
    # tree. And "setroot()" method can change the root of the tree or the subtree. 
    def getright(self):
        return self.rightchild

    def getleft(self):
        return self.leftchild

    def getroot(self):
        return self.root

    def setroot(self, newroot):
        self.root = newroot

# print mytree.rightchild.rightchild.getroot()
# print mytree.right.right.getright()
# print mytree.rightchild.getroot()
# print mytree.root
# print mytree.getleft()
#preorder(mytree)
