# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Naive option - keep ndes in a visited set - time and space are both N

option 2 - since length<= 1000 keep counter and if exceeding 1000 it means there's a cycle - will always take 1k steps and won't address 
the general problem with size limit bigger or unknown

if you iterating with two pointers one at 2x speed. at some point without a loop the faster pointer will reach none
with a loop one of two options
fast, slow

next step slow move 1 and fast move two they' will be in the same place

or fast, empty, slow - 

on other words with a loop, the faster will be behind the slow pointer and with each step the gap is narrowed by one - at some point they will meet

Aprroach: Two pointers at 1x and 2x speed
Invariant: No loop faster will reach a dead end. with loop at somepoint the fast will be behind the slow and close the gap by one each iteration 
until meeting at some point
Space: O(1)
Time: O(N)
Edge case:

empty list

"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detetcs cycle in a linked list

        Runs in linear time and constant space
        """

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # Fast reached the end of the list == no loops
        return False

        