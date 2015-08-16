a = [1,2,3]
def total (series):
 b=0
 for i in series:
  b = b + i
 return b
def noElements(series):
 for i in series:
  pass
 return i
def average(total, size):
 return total/size
print average(total(a), noElements(a))
