#Uses python2
"""
A Simple Program for Coursera  Algorithmic Toolbox

 & The Last Digit of a Large Fibonacci Number & 
Given an integer n, find the last digit of the nth 
Fibonacci number Fn.

Author: Lynn Lau
Date: 2016/07/27
""" 
''' Naive Algorithm '''
def Calc_Fib_Lst(n):
	FibList = [0,1]
	#print FibList
	if n == 0:
		return FibList[0]		
	elif n == 1:
	    return FibList[1]				
	for n in range(2,n+1):
		result = FibList[n-1] + FibList[n-2]
		FibList.append(result)
	#print FibList
	return FibList[n]%10

m = int(raw_input(''))
print Calc_Fib_Lst(m)

''' Smart Algorithm '''
def Calc_Fib_Lst(n):
	FibList = [0,1]
	#print FibList
	if n == 0:
		return FibList[0]		
	elif n == 1:
	    return FibList[1]				
	for n in range(2,n+1):
		result = FibList[n-1]%10 + FibList[n-2]%10
		FibList.append(result)
	#print FibList
	return (FibList[n])%10

m = int(raw_input(''))
print Calc_Fib_Lst(m)
