#Uses python2
def GCD(a, b):
	while b != 0:
		c = a%b
		a = b
		b = c
	return a

def LCM(a, b):
	Least_Common_Multipule = a*b/GCD(a,b)
	return Least_Common_Multipule

Nums = raw_input('').split()
gcd =  GCD(int(max(Nums)), int(min(Nums)))
print LCM(int(max(Nums)), int(min(Nums)))