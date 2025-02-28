import numpy as np
import random as rd




def binary_search(sorted_ar,v):
	#Sorted array as an input
	if len(sorted_ar) == 0:
		return None
	elif len(sorted_ar) == 1:
		if sorted_ar[0] == v:
			return 0
	else:
		middle = len(sorted_ar)//2 - 1
		left = sorted_ar[:middle+1]
		right = sorted_ar[middle+1:]
		if sorted_ar[middle] >= v:
			return binary_search(left,v)
		elif sorted_ar[middle] < v:
			try:
				return binary_search(right,v) + middle + 1
			except TypeError:
				return None
