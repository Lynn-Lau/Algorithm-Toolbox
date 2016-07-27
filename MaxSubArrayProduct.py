# Uses python2
"""
  Program for Coursera   Algorithm Toolbox
  Given a sequence of non-negative integers
  a0,…,an−1, find the maximum pairwise produc

  Author: Lynn Lau
  Date: 2016/07/25
"""

N = int(raw_input(''))
n = raw_input('')
List = [int (x)  for x in n.split()]
#print List

FirstMaximumNum = max(List)
List.remove(FirstMaximumNum)
SecondMaximumNum = max(List)

#print FirstMaximumNum
#print SecondMaximumNum
result = SecondMaximumNum * FirstMaximumNum
print result

""" Using for loop makes excution time over the
    limit time."""
#result = 0
#for i in range(0, N):
#	for j in range(i+1, N):		
#		if List[i]*List[j] > result:
#		    result = List[i]*List[j]
#print result
 