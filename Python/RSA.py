import numpy as np
p1 = 0
p2 = 0
phi = 0
modulus = 0
def breakString(str):

	no = []
	for i in range(0, len(str)):
		no.append(ord(str[i]))
	return no
	
def generatePrime():
	p = 0
	while True:
		a = np.random.randint(2, 20)
		#print("{} is our test number".format(a))
		for i in range(2, np.around(np.sqrt(a)).astype(int) +1):
			#print(i)
			if a % i == 0:
				#print("{} divisible by {}".format(a, i))
				break
		else:
			print("{} is prime".format(a))
			p = a
			break
		
	return p
def generateModulus():
	global p1 
	p1 = generatePrime()
	global p2 
	p2 = generatePrime()
	global modulus
	modulus = p1*p2
	
def phiN():
	ph = (p1-1)*(p2-1)
	global phi
	phi = ph


def generateKeys():
	e = np.random.randint(2, phi-1)
	print(e)
	q = []
	r = []
	r.append(e)
	q.append(modulus//e)
	r.append(modulus%e)
	while True:
		if(r[-1] == 1):
			break
		else:
			
		
	print("quotient {}, remainder {}".format(q,r))
	
 
def encrypt():{}

def decrypt():{}
#print breakString(raw_input("enter"))
#e = generatePrime()
generateModulus()
print(modulus)
phiN()
print(phi)
generateKeys()

