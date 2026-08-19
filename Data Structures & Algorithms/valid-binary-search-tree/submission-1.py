# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Approach: when visiting a node, send  the limits (starting with -1001, 1001). the right sub-tree limit is parent_floor, parent_val and the left sub-tree limits are parent_val, parent_ceiling
return true for null, any invalid subtree, invalidate the whole tree
Invariant:when left anf right sub tree ara valid trees with all subtrees values are equal or greater than any left ancestrs and equal or smaller than any right ansector
Preservation: root is a valid tree if left and right are valid subtrees and root calue is betwen left ancestors to right ancestors
Consequence: tree is valid
Time: O(N)
Space: O(H) <= O(N) -- recursion stack
Edge cases:
none

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=-1001, ceiling=1001) -> bool:
        """
        returns if the given tree is a valid binary search tree
        """
        if root is None:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False

        if not self.isValidBST(root=root.left, floor=floor, ceiling=root.val):
            return False
        if not self.isValidBST(root=root.right, floor=root.val, ceiling=ceiling):
            return False

        return True

"""
 [2,1,3] 

 2, -1000, 1000

    1, -1000, 2

    3, 2, 1000
"""


        