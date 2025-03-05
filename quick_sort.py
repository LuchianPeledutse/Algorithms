import random as rd 



def Partition(A,start,end):
	#to sort entire A is to sort A from 0 to len(A)-1
	if start < end:
		p = rd.randint(start,end)
		A[end],A[p] = A[p],A[end]
		p_el = A[end]
		p = start
		for ind in range(start,end):
			if A[ind] <= p_el:
				A[p],A[ind] = A[ind],A[p]
				p += 1
		A[end],A[p] = A[p],A[end]
		return p

def QuickSort(A,start,end):
	if start < end:
		pivot_index = Partition(A,start,end)
		QuickSort(A,start,pivot_index-1)
		QuickSort(A,pivot_index+1,end)



some_ar = [rd.randint(1,101) for _ in range(100000)]
print(some_ar)
QuickSort(some_ar,0,len(some_ar)-1)
print(some_ar)