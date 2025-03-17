import random as rd 
import numpy as np

def naive(A,B):
	#check whether they satisfy the necessary conditions
	if len(A[0]) != len(B):
		return ValueError('Such matrices cannot be multiplied')
	else:
		N = len(A)
		K = len(A[0])
		M = len(B[0])
		return [[sum([A[i][k]*B[k][j] for k in range(K)]) for j in range(M)] for i in range(N)]




def test(N = 10):
	for _ in range(N):
		R = rd.randint(1,10)
		C = rd.randint(1,10)
		Mutual = rd.randint(1,10)
		A = [[rd.randint(1,101) for _ in range(Mutual)] for _ in range(R)]
		B = [[rd.randint(1,101) for _ in range(C)] for _ in range(Mutual)]
		my_naive = np.array(naive(A,B))
		the_numpy = np.array(A)@np.array(B)
		if np.array(my_naive).reshape(-1).tolist() == (the_numpy).reshape(-1).tolist():
			print(f'TEST #{_+1} PASSED')
		else:
			print('###WRONG###')
			print('My_mul')
			print(my_naive)
			print('Np_mul')
			print(the_numpy)
			break
test(N = 100000)




