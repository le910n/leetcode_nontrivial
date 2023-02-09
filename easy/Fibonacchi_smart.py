import unittest
import time
from typing import List

# in such case the memoirising does not have such an immense effect

def fib_cache(N: int) -> int:
	cache = {}
	if N in cache.keys():
		return cache[N]

	if N < 2:
		return N 

	else:
		result = fib_cache(N-1) + fib_cache(N-2)
		cache[N] = result
		return result

def fib(N: int) -> int:
	return fib(N-1) + fib_cache(N-2) if N >= 2 else N


class fib_time_test(unittest.TestCase):

	def test_time_no_cache(self):
		test_input = 25

		start_time = time.time()
		fib_output = fib(test_input)
		no_cache_time = time.time() - start_time

		start_time = time.time()
		fib_cache_output = fib(test_input)
		cache_time = time.time() - start_time
		print(f' no cache time: {no_cache_time} sec | cache time: {cache_time} sec')
		self.assertGreater(no_cache_time, cache_time, f'{no_cache_time} sec | {cache_time} sec')

if __name__ == '__main__':
	unittest.main()

