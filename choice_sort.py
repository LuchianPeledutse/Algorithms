import random as rd
#random for testing
#choice sort inplace
#the time complexity is O(n^2)

def choice_sort(A):
	for i in range(len(A)-1):
		the_min = A[i]
		for j in range(i+1,len(A)): #whenever there is such a thing time complexity is probably O(n^2)
			if A[j]<the_min:
				next_the_min = A[j]
				A[j] = the_min
				the_min = next_the_min
		A[i] = the_min
	return A

#testing.
test_list = [[rd.randint(1,99) for _ in range(10)] for _ in range(10)]
for one_list in test_list:
	print(f'Initial_list: {one_list}')
	py_sort = list(sorted(one_list))
	my_sort = choice_sort(one_list)

	print(f'Python_sorted: {py_sort}')
	print(f'My_sorted:{my_sort}')
	if my_sort != py_sort:
		print('######################--WRONG--##################')
	print('\n\n')

