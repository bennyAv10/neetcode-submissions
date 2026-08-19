# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: null is zero height. non-null is max hild + 1
Invariant: when coming back from visiting childred their height is correct
Preservation: the height of current sub-tree is 1+max
Consequence: This alfgorithm is correct
Time: O(N) - number the tree nodes
Space: O(H) <= O(N) due to the stack
Edge cases:
null
single child
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

"""
exanmple 1

1
    2
        none ->0
        none ->0
    -> 1
    3
        4 -> 1
        none -> 0
    -> 2
-> 3

"""
        