# Uses python2

# binary search

import sys

def my_binary_search(value, low, high, keys):

    midValue = int((low + high)/2) + low
    for key in keys:
        if key == value[midValue]:
            return midValue
        else:
            if key < value[midValue]:
                high = midValue - 1
                # return my_binary_search(value, low, midValue-1, key)
            else:
                low = midValue + 1
                # return my_binary_search(value, midValue+1, high, key)
        key = key + 1

if __name__ =='__main__':
    valueInput = list(map(int, raw_input().split()))
    number = valueInput[0]
    value = valueInput[1: :1]
    keyInput = list(map(int, raw_input().split()))
    keys = keyInput[1: :1]
    low = 0
    high = number-1

    print my_binary_search(value, low, high, keys)
    # print number
    # print value
    # print keys
    # print low
    # print high
