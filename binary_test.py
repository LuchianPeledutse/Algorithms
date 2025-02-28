from binary_search import binary_search
from linear_search import linear_search
import random as rd



def test(N = 10):
	for ep in range(N):
		SHAPE = rd.randint(1,100)
		some_ar = [rd.randint(1,1000) for _ in range(SHAPE)]
		some_ar.sort()
		v = rd.randint(1,1000)
		l_search = linear_search(some_ar,v)
		b_search = binary_search(some_ar,v)
		print(f'TEST #{ep+1}')
		if l_search == b_search:
			print('PASSED')
		else:
			print('###WRONG###')
			print(v)
			print(some_ar)
			print(l_search,b_search)
			break



test(N = 100000)