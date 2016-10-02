def affine(x, a, b, m):
	return chr(((a*(ord(x.lower())-97) +b)%m)+97)
def generateCycle(init_letter, a, b, m):
	cycle =[init_letter.lower()]
	i = 0
	while True:
		letter = affine(cycle[i], a, b, m)
		if(letter == cycle[0]):
			break
		else:
			cycle.append(letter)
			i = i+1
		
	return cycle
def getallCycles(a, b, m):
	cycles = []
	letters = []
	for i in range(0,26):
		letter = chr(i+97)
		if not letter in letters:
			cycle = generateCycle(letter, a, b, m)
			cycles.append(cycle)
			for l in cycle:
				letters.append(l)
		else:
			pass
	return cycles
def cycleLengths(a,b, m):
	#for i in range(0,m):
	all_cycles = getallCycles(a,b,m)
	#print("b={}".format(b))
	#print(all_cycles)
	lengths = []
	for j in all_cycles:
		lengths.append(len(j))
	#print(lengths)
	return ("a={}, b={}, cycle lenghts ={}".format(a,b,lengths))
	
#print(affine('A', 5, 8, 26))
#print(generateCycle("A",5,8,26))
print(getallCycles(5,8,26))
#coprime26 = [1,3,5,7,9,11,15,17,19,21,23,25]
#for j in coprime26:
#	#print("a={}".format(j))
#	for i in range(0,26):
#		print(cycleLengths(j, i, 26))