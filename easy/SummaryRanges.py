import unittest
from typing import List

def summaryRanges(nums: List[int]) -> List[int]:
	# simple corner case for the empty entry
	if not nums:
		return None
	# main case
	ans = []
	left = 0
	for right in range(len(nums)):
		if (right == len(nums)-1) or (nums[right] + 1 != nums[right + 1]):
			if left==right:
				ans.append(f'{nums[left]}') # could be nums[right], lol
			else:
				ans.append(f'{nums[left]}->{nums[right]}')
			left = right+1
	return ans


class SummaryRangesTests(unittest.TestCase):
	def test_1(self):
		input_ = [0,1,2,4,5,7]
		output_ = ["0->2","4->5","7"]
		self.assertEqual(summaryRanges(input_), output_, 'Should equal.')
		

	def test_2(self):
		input_ = [0,2,3,4,6,8,9,1000]
		output_ = ['0', '2->4', '6', '8->9', '1000']
		self.assertEqual(summaryRanges(input_), output_, 'Should equal.')


if __name__ == '__main__':
	unittest.main()
