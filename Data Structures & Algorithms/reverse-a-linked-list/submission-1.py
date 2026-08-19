"""
Approach: Recursion (just to practice). 
Complexity: Time: N Space N (Stack depth)
Invariant: each stack frame gets orig_head reversed_head. 


orig_head, new head
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverseListRecursion(self, orig_head: ListNode|None, reversed_head: ListNode|None) -> ListNode|None:
        if orig_head is None:
            return reversed_head
        
        next_orig = orig_head.next

        orig_head.next = reversed_head

        return self._reverseListRecursion(next_orig, orig_head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        given list x1->x2->...->x(n-1)->xn
        return the reversed list xn->x(n-1)->...->x2->x1
        """
        return self._reverseListRecursion(head, None)
