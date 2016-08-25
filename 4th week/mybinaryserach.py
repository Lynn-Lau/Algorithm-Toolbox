# Uses python2
# -*- coding: utf-8 -*-
# binary search
'''
A simple program for Coursera Data structures and Algorithms

Author:Lynn Lau
Date:2016/08/24
'''

import sys


def my_binary_search(value, key):

    low = 0
    high = len(value) - 1
    while(low <= high):
        mid = (low + high)/2
        midval = value[mid]

        if midval < key:
            low = mid + 1
        elif midval > key:
            high = mid - 1
        else:
            return mid

    return -1

if __name__ =='__main__':

    data1 = list(map(int, raw_input().split()))
    # values list
    data2 = list(map(int, raw_input().split()))
    # keys list
    n = data1[0]
    m = data2[0]
    # result = list()
    a = data1[1 : m + 1]
    for x in data2[1: m + 1]:
        # replace with the call to binary_search when implemented
        print my_binary_search(a, x)