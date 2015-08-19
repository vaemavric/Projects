import math
def primeFactorise(n):
 factors = [n]
 for i in range(2, int(math.sqrt(n))+1):
  if n % i == 0:
   factors.append(i)
   factors.append(n/i)
 factors.sort()
 factors.reverse()
 remove = []
 for e in factors:
  i = 0
  while (factors.index(e) + i +1  < len(factors)):
   if e % factors[factors.index(e) +1 +i] == 0:
    if(factors.count(e) == remove.count(e)+1) and factors.count(e) > 1 and factors.count(e) != 1:
     pass
    else:
     remove.append(e)
     break
   i +=1
 for e in remove:
  factors.remove(e)
 powers = []
 for e in factors:
  i = 0
  a = n
  while a%e ==0 :
   a //= e
   i += 1
   if n == 1:
    break
  powers.append(i)
 factors.reverse()
 powers.reverse()
 print factors
 print powers
primeFactorise(int(raw_input("Type number to factorise:\n")))
