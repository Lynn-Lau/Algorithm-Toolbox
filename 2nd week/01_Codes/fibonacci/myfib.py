# Uses python2
"""
 A Simple Program for Coursera  Algorithmic Toolbox

 Cumpute the Fibonacci numbers. Fibonacci nubers are defined
 as F0=0,F1=1,F2=1,F3=2,...,Fi=F(i-1)+F(i-2). The run time of
 the codes should less than 5 seconds.
 n < 50

 Author: Lynn Lau
 Date: 2016/07/27 
"""

""" This is a naive algorithm """

def Calc_Fib(n):
	if n == 0:
		return n
	elif n == 1:
		return n
	elif n >= 2:
		result = Calc_Fib(n-1) + Calc_Fib(n-2)
		return result
n = int(raw_input(''))
print Calc_Fib(n)

""" This is a smart algorithm """
def Calc_Fib(n):
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
	return FibList[n]

m = int(raw_input(''))
print Calc_Fib(m)