# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: recursively get left and right sub-tree. if only ne is none or val is differnt not it's not equivalent otherwise if both subtrees are equivalent they're too
Invariant: assuming both childrent are equivalent
Preservation: if bth values are the same the current trees are equivalent
consequence: we validated both trees are equivalent
Time: (N)
Space: O(H) (num of nodes <= 100 so it safe)
edge cases:
none
only one has childrent
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Are both trees equivalent
        """
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
test:

4, 7 -- 4, null, 7

4, 4

    7, none --> False 


"""
        