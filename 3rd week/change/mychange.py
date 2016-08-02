#Uses python2

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