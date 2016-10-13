# -*- codding: utf-8 -*-

# Author:Lynn Lau
# Date:2016/10/13
# Language: Python 2.7.11
import os
from BinTree import BinaryTree
"""
 Treversal Tree
 This code blocks will traversal the tree. In "preorder()" traversal method,
 we visit the root node first, then recursively do the preorder traversal of
 the left subtree, then the right tree. While the "inorder()" traversal method,
 we visit the left subtree, then root node and then right subtree recursivly.
 In "postorder()", we visit the right subtree, then the right subtree and 
 followed by the root node.
"""
def preorder(tree):
    """ Root Node, Left Subtree, Right Subtree """
    if tree:
        print(tree.getroot())
        preorder(tree.getleft())
        preorder(tree.getright())
    
def postorder(tree):
    """Left Subtree, Right Subtree, Root Node """
    if tree != None:
        postorder(tree.getleft())
        postorder(tree.getright())
        print (tree.getroot())

def inorder(tree):
    """ Left Subtree, Root Node, Right Subtree """
    if tree != None:
        inorder(tree.getleft())
        print(tree.getroot())
        inorder(tree.getright())

if __name__ == '__main__':
    """ main function
        Creat binary instance and traversal it.
    """
    mytree = BinaryTree('a')
    mytree.insertleft('b')
    mytree.leftchild.insertright('d')
    mytree.insertright('c')
    mytree.rightchild.insertleft('e')
    mytree.rightchild.insertright('f')
    # print mytree.getroot()
    # preorder(mytree)
    # inorder(mytree)
    postorder(mytree)

