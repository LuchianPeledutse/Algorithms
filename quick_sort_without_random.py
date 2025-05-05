import random as rd

#patition of A start ind = p, end ind = r
def partition(A,p,r):
	#p<r
	i = p-1
	pivot = A[r]
	#main loop
	for j in range(p,r+1):
		if A[j] <= pivot:
			i = i + 1
			A[j],A[i] = A[i],A[j]
	#connect the pivot to other elements
	return i 


def quicksort(A,p,r):
	if p < r:
		q = partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)


