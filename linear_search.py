#linear_search


def linear_search(the_ar,v):
	ind = 0
	for j in range(len(the_ar)):
		if the_ar[j] == v:
			return ind
		else:
			ind += 1
	return None