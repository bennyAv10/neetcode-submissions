# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: we visit in order and keep tracking on nodes so far both as an argument and retunred value. when left-subtree retruned if smaller elements are k-1 current node is kth
Invariant: 1. when vising a node we know how many smaller non-decendance nodex are there and 2. we know the size of each subtree when gettin gback from visit
Preservation: 1. when calling left sub-tree it's the same number of non-decendances smaller nnodes and for right sub-tree is adding left subtree size and root
    2. when getting back to parent we know the size of this subtree (size-right+size-left+1)
consequence: base-1: when calling root, there are 0 smaller non decandands base-2: when calling leaves size of both left and right are 0. with the preservation we know the Kth element
Time: we need to visit max(H, K) - worst case O(N)
Space: O(H) 
Edge cases:
none
single child 
"""
class Solution:    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the Kth smallest value in a BST with all unique values
        """
        def visit(smaller_nodes: int, root: TreeNode | None) -> tuple[int | None, int | None]:
            """
            returns [None or the Kth value, number of nodes in the subtree]
            """
            if root is None:
                return None, 0
            
            k_val, left_size = visit(smaller_nodes, root.left)
            if k_val != None:
                return k_val, None

            if smaller_nodes + left_size == k-1:
                return root.val, None
            
            k_val, right_size = visit(smaller_nodes+left_size+1, root.right)
            if k_val != None:
                return k_val, None
            
            return None, right_size+left_size+1

        return visit(smaller_nodes=0, root=root)[0]

"""
Input: root = [2,1,3], k = 1


0, 2
    0, 1
        0, None --> None, 0
    --> 
"""


            
        