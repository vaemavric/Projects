num = 0 
test = ""
revsersetest = ""
for i in range(100,1000):
 for e in range(100,1000):
  test = str(e * i)
  reversetest =  test[::-1]
  if test == reversetest and int(test) >num:
   num = int(test)
print num
