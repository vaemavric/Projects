import time
filename = raw_input("type filename \n >")
txt = open(filename, "r")
def file_len():
 with open(filename) as f:
  for i, index in enumerate(f):
   pass
  return i
def printline(lines, lineval):
 for i in range(lines): 
  line = txt.next()
  if i == lineval - 1:
   print line
  elif lineval>lines:
   print "line %s does not exist in file %s" % (lineval, filename)
   break
printline(file_len()+1, input("type line number \n >"))
txt.close()

