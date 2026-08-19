# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approaches:
1. Push the floor of n/2 last elements into stack. iterate over the first half and push in the opposite order from the stack. T:N S: N
2. half the list. reverse the 2nd half and merge them. T: N. Space: 1 --> going with this approach as it's more efficient and will teach me more
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        size = 0
        while current:
            current =current.next
            size+=1

        second_head = head
        for i in range(math.ceil(size/2)):
            prev = second_head
            second_head = second_head.next
        prev.next = None

        prev = None        
        while second_head:
            next = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = next
        
        second_head = prev
        first_head = head

        current = ListNode()

        while first_head or second_head:
            if first_head:
                current.next = first_head
                current = current.next
                first_head=first_head.next 
                current.next = None
            if second_head:
                current.next = second_head
                current = current.next
                second_head = second_head.next
                current.next = None
        
"""
[0, 1, 2, 3, 4, 5, 6]
size = 7
second_head -> 0
ceil(7/2) = 4

second_head -> 4

[0,1,2,3]
[4,5,6]

prev=none
second_head=4
    n->5
    4.next -> none
    prev->4
    sh ->5

    n->6
    5.next->4
    prev->5
    sh->6

    n->none
    6.next->5
    prev->6
    sh->none

fh -> 0,1,2,3
sh -> 6,5,4

current -> dummy

    current -> dummy, 0
    fh -> 1,2,3


"""






        