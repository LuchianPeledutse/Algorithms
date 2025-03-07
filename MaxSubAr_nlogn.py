#First we create a function that firds max sub-array that 
#crosses the mid point of the array

def MaxSubCrossing(A,start,middle,end):
	#We assume that A has at least 2 elements
	left_sum = float('-inf')
	left_max = None
	current_sum = 0
	for left_ind in range(middle,start-1,-1):
		current_sum += A[left_ind]
		if current_sum > left_sum:
			left_sum = current_sum
			left_max = left_ind

	right_sum = float('-inf')
	right_max = None
	current_sum = 0
	for right_ind in range(middle+1,end+1):
		current_sum += A[right_ind]
		if current_sum > right_sum:
			right_sum = current_sum
			right_max = right_ind

	return (left_max,right_max,left_sum + right_sum)


def MaxSub(A,start,end):
	if start == end:
		return start,end,A[start]
	else:	
		mid_point = (start+end)//2

		cross_start,cross_end,cross_sum = MaxSubCrossing(A,start,mid_point,end)
		left_start,left_end,left_sum = MaxSub(A,start,mid_point)
		right_start,right_end,right_sum = MaxSub(A,mid_point+1,end)

		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_start,left_end,left_sum
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return right_start,right_end,right_sum
		else:
			return cross_start,cross_end,cross_sum

