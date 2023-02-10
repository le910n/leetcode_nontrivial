import unittest

# define the object we'll be working with 

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def MergeSortedList_recursion(l1, l2):
	"""
	Processes the vals and falls into the recursion.
	Space complexity: O(n1 + n2).
	Time complexity: O(n1 + n2).
	"""
	# corner cases
	if not l1:
		return l2
	if not l2:
		return l1
	# main case
	if l1.val > l2.val:
		l1.next = MergeSortedList_recursion(l1.next, l2)
		return l1
	else:
		l2.next = MergeSortedList_recursion(l2.next, l1)
		return l2


def MergeSortedList_iteration(l1, l2):
	"""
	Iterative version, using the Sentinel Node. 
	Seems to work with O(1) additional space.
	"""
	# corner cases
	if not l1:
		return l2
	if not l2:
		return l1

	# create the sentinel
	sentinel = ListNode(-1)
	# put the pointer starting on the sentinel
	prev = sentinel
	# iterate over the lists
	while l1 and l2:
		# choose
		if l1.val >= l2.val:
			prev.next = l1
			l1 = l1.next
		else:
			prev.next = l2
			l2 = l2.next
		# move the pointer
		prev = prev.next
	# add the remaining tail of the list
	prev.next = l1 if l1 is not None else l2
	return sentinel.next




# testing area
#class TestMergeSortedList(unittest.TestCase):
#
#	def test_1(self):
#		input_1 = ListNode(val = 0, next = ListNode(val = 1, next = ListNode(val = 15, next=None)))
#		input_2 = ListNode(val = 1, next=ListNode(val = 2, next = ListNode(val = 15, next=ListNode(val = 17, next=None))))

#   That is long and tedious to write such tests manually
#   May be there is special function to construct linked lists?

#		
#
# main scope
#if name == '__main__':
#	unittest.main()