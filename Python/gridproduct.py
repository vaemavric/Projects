import time
start = time.time()
L = []
def file_len(filename):
 with open('{}'.format(filename)) as f:
  for i, index in enumerate(f):
   pass
  i += 1
  return i

#create grid from file
def cGrid():
 try:
  inp = open('grid.txt', 'r')
 except:
  print('file does not exist')
 for i in range(file_len('grid.txt')):
	line = inp.next()
	L.append(line)

#multiply grid
def mGrid():
 m = 0
 M = 0
 #x & y
 for i in range(19):
  for j in range(16):
   m = int(L[i][j])*int(L[i][j+1])*int(L[i][j+2])*int(L[i][j+3])
   if m>M:
    M=m
   m = int(L[j][i])*int(L[j+1][i])*int(L[j+2][i])*int(L[j+3][i])
   if m>M:
    M=m
 #diagonal
 for i in range(16):
  for j in range(16):
   m = int(L[i][j])*int(L[i+1][j+1])*int(L[i+1][j+2])*int(L[i+3][j+3])
   if m>M:
    M=m
   m = int(L[i+3][j])*int(L[i+2][j+1])*int(L[i+1][j+2])*int(L[i][j+3])
   if m>M:
    M=m
 print(M)
cGrid()
L =  [i.split() for i in L]

mGrid()
elapsed = (time.time() - start)
print elapsed