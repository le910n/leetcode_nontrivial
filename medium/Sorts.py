import unittest
from unittest_prettify.colorize import (
    colorize,
    GREEN,
)

from typing import List
import random
import numpy as np 

def BubbleSort(nums:List[int]) -> None:
	"""
	Accepts nums: list of ints, sorts that inplace with a Bubble Sort.
	No particular features, it's easy.
	"""
	N = len(nums)
	# corner case
	if N < 2:
		return nums


	# repeatable part
	while True:
		num_inversions = 0
		left, right = 0, 1
		while right < N:
			if nums[left] > nums[right]:
				nums[left], nums[right] = nums[right], nums[left]
				num_inversions += 1
			else:
				left += 1
				right += 1
		if num_inversions == 0:
			return 

def InsertionSort(nums: List[int]) -> None:
	"""
	Accepts nums: list of ints, sorts it inplace with an Insertion Sort.
	Works well for almost-sorted arrays. Works nice for the small arrays.
	"""
	for i in range(1, len(nums)):
		pt = i
		while pt > 0 and nums[pt - 1] > nums[pt]:
			nums[pt-1], nums[pt] = nums[pt], nums[pt-1]
			pt -= 1



@colorize(color=GREEN)
class SortTest(unittest.TestCase):

	# test orchestrating line
	sort_type = InsertionSort


	def test_1(self, sort_type=sort_type):

		"""Typical random int numbers example"""

		test_input = [2, 1, 2, 5, 34, 14, 3, 4, 5, 6, 3]
		sort_type(test_input)
		test_output = [ 1,  2,  2,  3,  3,  4,  5,  5,  6, 14, 34]
		msg = f'{sort_type}: {test_input} is the processed result. Must be {test_output}'
		self.assertEqual(test_input, test_output, msg)

	def test_2(self,sort_type=sort_type):

		"""Already sorted example"""

		test_input = [ 1,  2,  2,  3,  3,  4,  5,  5,  6, 14, 34]
		sort_type(test_input)
		test_output = [ 1,  2,  2,  3,  3,  4,  5,  5,  6, 14, 34]
		msg = f'{sort_type}: {test_input} is the processed result. Must be {test_output}'
		self.assertEqual(test_input, test_output, msg)

	def test_short(self,sort_type=sort_type):
		''' Length = 2 example '''
		test_input = [2, 1]
		sort_type(test_input)
		test_output = [1, 2]
		msg = f'{sort_type}: {test_input} is the processed result. Must be {test_output}'
		self.assertEqual(test_input, test_output, msg)

	def test_one_length(self,sort_type=sort_type):
		''' Length = 1 example '''
		test_input = [2]
		sort_type(test_input)
		test_output = [2]
		msg = f'{sort_type}: {test_input} is the processed result. Must be {test_output}'
		self.assertEqual(test_input, test_output, msg)

	def test_really_long(self,sort_type=sort_type):
		''' Long example '''
		test_input = [random.randint(1, 10000) for _ in range(int(1e3))]
		sort_type(test_input)
		test_output = sorted(test_input)
		msg = f'{sort_type}: {test_input[:10]} is the processed result. Must be {test_output[:10]}'
		self.assertEqual(test_input, test_output, msg)


	def test_empty(self,sort_type=sort_type):
		''' Empty example '''
		test_input = []
		sort_type(test_input)
		test_output = []
		msg = f'{sort_type}: {test_input} is the processed result. Must be {test_output}'
		self.assertEqual(test_input, test_output, msg)


if __name__ == '__main__':
	print(f'Running with the {SortTest.sort_type.__name__} sort...'.upper())
	unittest.main(verbosity=2)

