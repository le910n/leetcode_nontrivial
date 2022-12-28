# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # corner case in case we meet the test for []
        if head is None:
            return head

        # main loop
        # first of all, use sentinel
        sentinel = Node(-1, None, head, None)
        # flag for the usage of ending sentinel
        end_sentinel = False
        # set the running pointer 
        pt = sentinel
        # add the ending sentinel and change the flag if the layer is first-drop
        if head.next is None:
            head.next = Node(-1, head, None, None)
            end_sentinel = True

        # while we can move the pointer, insert layers from below via REWIRING
        while pt.next:
            # move horizontally if no children
            if not pt.child:
                pt = pt.next
            # move back, set the start_window and the end_window pointer
            else:
                pt_start = pt.child # create the one-level-lower pointer
                pt_end = pt.child 
                while pt_end.next:
                    pt_end = pt_end.next # move the end pointer to the end of the newfound layer
                
                # rewire, inserting the lower layer between pt and pt.next (end_sentinel in some cases)
                desc = pt.next
                pt.next = pt_start
                pt_start.prev = pt
                pt_end.next = desc
                desc.prev = pt_end
                pt.child = None
                pt = pt.next

        # clear up the end_sentinel mess if there is one
        if end_sentinel:
            pt = pt.prev
            pt.next = None
                
        # return
        return sentinel.next
