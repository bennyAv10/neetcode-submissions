"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Approach: first iteration just create the list without assining the random pointers, but create old too new map. 2nd iteration go over the original list and set the equvalent list in the new list by the map
Invariant: nor reallt needed here. each step is pretty basic
Time: O(N)
Space: O(N) for the map
Edge cases:
empty list
random is null
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current_orig = head
        new_dummy_head = Node(x=-1)
        current_new=new_dummy_head
        orig_to_new = {}

        while current_orig:
            current_new.next = Node(x=current_orig.val)

            orig_to_new[current_orig] = current_new.next

            current_orig = current_orig.next
            current_new = current_new.next

        current_orig = head
        while current_orig:
            if current_orig.random is not None:
                current_new = orig_to_new[current_orig]
                current_new.random = orig_to_new[current_orig.random]
            current_orig = current_orig.next

        return new_dummy_head.next

"""
[[3,null],[7,3],[4,0],[5,1]]

ndh = []
cn =[]

3,null
ndh =[],[3,null]

7,3
ndh = [],[3,null],7null,

4,0

5,1

bug 1: current_orig.none can be none
bug 2 forgot to promote current_orig
"""


        