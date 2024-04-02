# pollard.py

from auxiliary import gcd

def factor(n,b):
	""" Factor using Pollard's p-1 method """
	a = 2
	for j in range(2,b):
		a = a**j % n
	
	d = gcd(a-1,n)
	if 1 < d < n: return d
	else: return -1

def testFactor(n: int, s: int , d: int):

	while s < n and d == -1:
		s +=1
		d = factor(n,s)

	if d == -1:
		raise ValueError('No factor could be found')
	else:
		return (n,d,s)