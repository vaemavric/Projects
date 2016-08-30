fib = [1,1]
def fibn(n):
	if n == 1 or n == 2:
		return 1
	else:
		for i in range(1, n-1):
			fib.append(fib[i-1]+fib[i])
		return fib[-1]
n= input("Please enter a number:	")
print("The {}th fibonacci number is {}".format(n, fibn(int(n))))
		