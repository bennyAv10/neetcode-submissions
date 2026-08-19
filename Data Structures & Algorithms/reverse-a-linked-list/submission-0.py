"""
solution 1:
stack

invariant: at any point [head...i) is in reverse order in the stack and [i..end] is the rest of the stack

you push the prev to the stack

tkae it out of the stack with head init to stack top and next is always the next in stack

time N, space N

question asks for space 1

init head
invariant: you keep holding the head of remainng original list and head of new (reveresed) list

reversed_head = head
with each iteration:
    you make the head of orig the new head of reversed
    and the new head of orig the the next
stop when head is none

time n
space n
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None

        while head:
            next_head = head.next
            
            head.next = reversed_head
            reversed_head = head

            head = next_head

        return reversed_head

"""
test
[0,1,2,3]

init
head = [0,1,2,3]
r = None

s1
head = [1,2,3]
r = [0]

s2


"""