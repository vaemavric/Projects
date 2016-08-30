l = [8, 2, 4, 6, 7, 9, 1, 3, 6, 7, 0]
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#bubbleSort(l)
print(l)
def insertSort(al):
	for i in range(0, len(al)):
		for j in range(0, len(al)):
			if(al[i] > al[j]):
				al.insert(j, al.pop(i))
				print al
			else:
				pass

#insertSort(l)
def selectSort(li):

	for i in range(0, len(li)):
		a = li[0]
		for j in range(0, len(li)-i):
			if a > li[j]:
				a = li[j]
			else:
				pass#
		print len(li)-i
		li.insert(len(li)-1-i, li.pop(li.index(a)))
selectSort(l)
print l				