#Uses python2

user_input = raw_input()
#print user_input
alist = list()
blist = list()
Alist = raw_input().split()
for item in Alist:
	alist.append(int(item))
#print alist
Blist = raw_input().split()
for item in Blist:
	blist.append(int(item))
#print blist
#print user_input
alist.sort(reverse = True)
blist.sort()
#print alist
#print blist
product = list()
for i in range(0, int(user_input)):
	product.append(alist[i] * blist[i])
sum = 0
#print product
for item in range(0, int(user_input)):
	sum = sum + product[item]
print sum