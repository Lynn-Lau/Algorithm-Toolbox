#Uses python2
'''
A Simple Program for Coursera  Algorithmic Toolbox

The greatest common divisor GCD(a; b) of two non-negative 
integers a and b (which are not both equal to 0)
is the greatest integer d that divides both a and b.

Author: Lynn Lau
Date: 2016/07/17
'''
def GCD(a, b):
	while b != 0:
		c = a%b
		a = b
		b = c
	return a
	
Nums = raw_input('').split()
print GCD(int(max(Nums)), int(min(Nums)))