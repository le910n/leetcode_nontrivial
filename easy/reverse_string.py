import unittest
from typing import List

def reverse_string(s: List[str]) -> None:
	"""
	Reverse list of str inplace, attempt to use recursion.
	"""
	def helper(left, right):
		if left < right:
			s[left], s[right] = s[right], s[left] # think about the namespace
			helper(left+1, right-1)
	helper(0, len(s)-1)
	return s


class TestString(unittest.TestCase):

	def test_string_1(self):
		test_input = ["h","e","l","l","o"]
		test_output = ["o","l","l","e","h"]
		self.assertEqual(reverse_string(test_input),
						 	test_output,
						 	'Should match.')

	def test_string_2(self):
		test_input = ["H","a","n","n","a","h"]
		test_output = ["h","a","n","n","a","H"]
		self.assertEqual(reverse_string(test_input),
						 	test_output,
						 	'Should match.')

	def test_string_empty(self):
		test_input = []
		test_output = []
		self.assertEqual(reverse_string(test_input),
							test_output,
							'Should match.')


if __name__ == '__main__':
	unittest.main()

