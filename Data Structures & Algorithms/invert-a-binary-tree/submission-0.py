# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Invert definition: each substree recusrsively is switched left <-> right
Approach: post-order recusrion. you handle each sub-tree and them switch them. you stop qhen root is null
Invariant: assuming both sub-trees are inverted, 
Preservation: Switching them makes the current node inverted. same applies to the current node sibiling --> the node parent has both sub-trees inverted
Consequence: Eventually the whole tree is inverted
Time: O(N) one visit eacy node
Space: O(H) tree hegiht max O(N) (unbalanced tree)

Edge cases:
node with a single child

slight alternative: replace the val instead of nodes - current slution is better - value agnostic and clean for single child
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert binray tree recusrsively
        """
        if root is None:
            return None
        
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root

"""
test

example 1

root 1

    root 2
        root 4 --> same
        root 5 --> same
    5, 4
    root 3
        root 6
        root 7
    7, 6

"""
        