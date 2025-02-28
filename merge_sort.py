#merge  sort with complexity of O(nlogn)
import random as rd 

def Merge(A,p,q,r):
	#we know that 0<=p<=q<r<=N-1 where N = len(A)
	n1 = q-p+1
	n2 = r-q
	L = [1 for _ in range(n1)]
	R = [1 for _ in range(n2)]

	for k in range(n1):
		L[k] = A[k+p]
	for k in range(n2):
		R[k] = A[q+k+1]
	i,j = 0,0
	for k in range(p,r+1):
		if i + 1 > n1:
			A[k] = R[j]
			j += 1
		elif j + 1 > n2:
			A[k] = L[i]
			i += 1
		else:
			if L[i] <= R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1

def MergeSort(A,p,r):
	#We know that 0<=p<=r<=N-1
	if p < r:
		q = int((p+r)/2) #q satisfies the necessary conditions for Merge function
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)
#testing Merge-sort 



