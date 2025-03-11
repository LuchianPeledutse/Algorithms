


def KadMaxSubAr(some_ar):
	if len(some_ar) == 1:
		return some_ar[0]
	else:
		max_sum = current_sum = some_ar[0]
		for el in some_ar[1:]:
			current_sum = max(current_sum + el,el)
			max_sum = max(max_sum,current_sum)
		return max_sum