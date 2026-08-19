# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Approach: Iterative
Invariant: each iteration begins with the merged list either empty or sorted. list 1 and list2 are still sorted. and all numbers 
in the merged list are equal or smaller that list1 and list2 heads. at each step we just take the smaller of list 1 and 2 and make it 
the new tail of the merged list
Time: O(N)
Space: 1
Alternatives:
recusrion - same time but linear space
"""
class Solution:
    def _removeListHead(self, head: ListNode|None):
        old_head = head
        head=head.next
        old_head.next = None

        return old_head, head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode() #dummyhead
        current_merged = merged_head

        # if list1.val < list2.val:
        #     merged_head, list1 = self._removeListHead(list1)
        # else:
        #     merge_head, list2 = self._removeListItem(list2)

        while list1 or list2:
            if (list1 and not list2) or (list1 and (list1.val < list2.val)):
                current_merged.next, list1 = self._removeListHead(list1)
            else:
                current_merged.next, list2 = self._removeListHead(list2)
            current_merged = current_merged.next
        
        return merged_head.next


        