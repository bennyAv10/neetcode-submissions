# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approaches"
1. preserve the list before. push into queue until reaching right. right is now head. now, add from the queue and make it the new head until the queue is empty - Time: O(N). Space O(1) - we use the original nodes
Invariant: 1. phase 1. the queue has the nodes from head to i in the queue in order and i is the head (i<=right) 2. the retruned list has right to end same as original and i to right is the opposite original of head to i
Preservation: 1. adding the next node to the queue preserve the same assumption for i+1 2. poping left from the queue (FIFO) and make it the new head preserve the opposite ordet of i-1 to right
edge cases:
 left=right
 left >1
 left=1
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        orig_head = head

        i=1
        while i<left:
            i+=1
            head=head.next
                
        
        queue = collections.deque()
        while i<=right:
            queue.append(head)
            i+=1
            head = head.next
        
        while queue:
            next_node = queue.popleft()
            next_node.next = head
            head = next_node
        
        if left > 1:
            i=1
            prefix_head = orig_head
            while i< left-1:
                i+=1
                prefix_head=prefix_head.next
            
            prefix_head.next = head
            return orig_head
        else:
            return head

"""
[1,2,3,4,5], left = 1, right = 3

q=[]
h=1
i=1
    q=1
    h=2
i=2
    q=[1,2]
    h=3
i=3
    q=1,2,3
    h=4

q=[1,2,3]
    n = 1
    l=1,4,5
q=[2,3]
    n=2
    l=2,1,4,5
q=3
    n=3
    l=3,2,1,4,5

l=2 --> works
l=3

bug 1: 2nd loop forgot to increase i

"""


        


        