#Uses python2
'''
A Program for Data Structures and Algorithms(DSA) 

* Changing Money *
The goal in this problem is to find the minimum 
number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10. 

Author: Lynn Lau
Date: 2016/07/31
'''
def get_change(num):

	n1 = int(num/10)
	reminder10 = int(num%10)
	n2 = int(reminder10/5)
	reminder5 = int(reminder10%5)
	n3 = int(reminder5/1)
	n = n1 + n2 + n3
	return n

num = int(raw_input(''))
print get_change(num)