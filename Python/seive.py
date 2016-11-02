import math
import time
def factorise(n):
	for i in range (2, int(math.sqrt(n))+1):
		if n%i == 0:
			print i
init = time.time()
#factorise(5678902342349209)
fin = time.time()
taken = fin-init
print("Time taken: {}".format(taken))
print("soln: 197*28826915443397")