from merge_sort import MergeSort
import random as rd
import time


def n2_2_sum(S,x):
	#time complexity of this method is O(n^2)
	if len(S) < 2:
		return False
	else:
		N = len(S)
		for i in range(N-1):
			for j in range(i+1,N):
				if S[i] + S[j] == x:
					return True
	return False


def nlogn_2_sum(S,x):
	NN = len(S)
	MergeSort(S,0,NN-1)
	left = 0
	right = NN - 1
	while left < right:
		if S[left] + S[right] == x:
			return True
		elif S[left] + S[right] < x:
			left += 1
		elif S[left] + S[right] > x:
			right -= 1
	return False


