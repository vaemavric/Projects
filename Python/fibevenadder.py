def fib(lim):
 a = 1
 b = 2
 c = b
 total = 0
 while a < lim:
  print a
  if a % 2 ==0:
   total += a
  else:
   pass
  b += a 
  a = c
  c = b
 return total
print fib(4000000)
