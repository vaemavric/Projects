def funct(x):
	return x**(x/3)-2
def derivative(x, h):
	return ((funct(x+h)-funct(x)) /h)
def newtonraphson(a):	
	xn = [a]
	for i in range(0,1000):
		xn.append(xn[i]-(funct(xn[i])/(derivative(xn[i], 0.001))))
	print (xn[-1])
	print (funct(xn[-1])+2)
newtonraphson(100)
