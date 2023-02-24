from typing import Optional


# first, define the object we are working with 
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def insertion_sort(head: Optional[ListNode]) -> Optional[ListNode]:

	if not head or not head.next:
		return head
		

