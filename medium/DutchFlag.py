import unittest
from typing import List

def sortColours(nums: List[int]) -> None:
	"""
	Inplace sort the nums array such that 0 < 1 < 2 clusterwise.
	"""
	if not nums:
		return nums

	left, curr = 0, 0
	right = len(nums) - 1

	while curr <= right:
		if nums[curr] == 0:
			nums[curr], nums[left] = nums[left], nums[curr]
			curr += 1
			left += 1
		elif nums[curr] == 2:
			nums[curr], nums[right] = nums[right], nums[curr]
			right -= 1  
		else:
			curr += 1


class DutchFlagTest(unittest.TestCase):

	def test_1(self):
		test_input = [0, 0, 1, 1, 2, 2]
		sortColours(test_input)
		test_output = [0, 0, 1, 1, 2, 2]
		msg = f'Output must be: {test_output}. It is {test_input}'
		self.assertEqual(test_input, test_output, msg)

	def test_2(self):
		test_input = [2, 2, 1, 1, 0, 0]
		sortColours(test_input)
		test_output = [0, 0, 1, 1, 2, 2]
		msg = f'Output must be: {test_output}. It is {test_input}'
		self.assertEqual(test_input, test_output, msg)

	def test_3(self):
		test_input = []
		sortColours(test_input)
		test_output = []
		msg = f'Output must be: {test_output}. It is {test_input}'
		self.assertEqual(test_input, test_output, msg)
	def test_4(self):
		test_input = [0, 2, 0, 1, 0, 2, 0, 1, 2, 0]
		sortColours(test_input)
		test_output = [0, 0, 0, 0, 0, 1, 1, 2, 2, 2]
		msg = f'Output must be: {test_output}. It is {test_input}'
		self.assertEqual(test_input, test_output, msg)



if __name__ == '__main__':
	unittest.main()