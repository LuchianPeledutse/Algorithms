import random as rd
#numpy for testing
#choice sort inplace
#the time complexity is O(n^2)

def choice_sort(A):
	for i in range(len(A)-1):
		min = A[i]
		for j in range(i+1,len(A)-1): #whenever there is such a thing time complexity is probably O(n^2)
			if A[j]<min:
				next_min = A[j]
				A[j] = min
				min = A[j]
		A[i] = min
	return A



