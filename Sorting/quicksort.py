# -*-coding:utf-8-*-
# Data Structure and Algorithm, Quick Sort

# Author:Lynn Lau
# Date:2016/09/30
# Language:Python 2.7.11


def quick_sort(alist):
    qsort_rec(alist, 0, len(alist)-1)
    return alist


def qsort_rec(alist, leftmark, rightmark):

    left = leftmark
    right = rightmark

    if left >= right:
        return
    pivot = alist[left]
    while left < right:
        while left < right and alist[right] >= pivot:
            right -= 1
        if left < right:
            alist[left] = alist[right]
            left += 1

        while left < right and alist[left] <= pivot:
            left += 1
        if left < right:
            alist[right] = alist[left]
            right -= 1

    alist[left] = pivot
    qsort_rec(alist, leftmark, left-1)
    qsort_rec(alist, left+1, rightmark)

if __name__ == '__main__':

    data = raw_input('Please input some numbers:')
    numbers = list(map(int, data.split()))
    sorted_numbers = quick_sort(numbers)
    print sorted_numbers

