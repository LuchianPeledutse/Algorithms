#insertion sort non-decreasing or non-increasing

def insert_sort(the_ar,decrease = False):
	N = len(the_ar)
	for j in range(1,N):
		key = the_ar[j]
		i = j-1
		while i>=0 and (the_ar[i]>key if not decrease else the_ar[i] < key):
			the_ar[i+1] = the_ar[i]
			i -= 1
		the_ar[i+1] = key
	return the_ar