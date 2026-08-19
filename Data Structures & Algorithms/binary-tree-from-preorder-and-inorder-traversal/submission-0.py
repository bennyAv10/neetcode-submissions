# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: at every node, root is the first preorder node. since node values are unique, we can find its inorder index.
from that, we can find the left subtree in inorder (All the nodes before root). from that we know the size of both left and right sub tree.
from that we know the location of root, right, and left subtrees in both inorder and preorder
sub-alternatives: 
1. search: find root in inorder by linear search. linear every subtree - total N^2
2. inveretd inorder index:  constant every time. total linear. cost is linear space --> we'll use this approach
Invariant: when visiting subtree t we know t_start and t_end in both in_order and pre_order
Preservation: the steps described in the approach above shows we can prove the same for both left and right subtrees and that we know the root value
Consequence: we can restore the tree
Time: O(N)
Space: O(N)
Edge cases:
preorder\inorder of size 0 - return none
only one-subtree exist - will be handled by size 0 above
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = { inorder[i]:i for i in range(len(inorder))}

        def visit(pre_start: int, in_start: int, size: int) -> TreeNode | None:
            if size == 0:
                return None

            root = preorder[pre_start]
            root_in_index = inorder_index[root]
            left_size = root_in_index - in_start
            right_size = size - left_size - 1 # -1 for root

            root_node = TreeNode(val=root)
            root_node.left = visit(pre_start=pre_start+1, in_start=in_start, size=left_size)
            root_node.right = visit(pre_start=pre_start+left_size+1, in_start=in_start+left_size+1, size=right_size)

            return root_node

        return visit(0, 0, len(inorder))

"""
preorder = [1,2,3,4], inorder = [2,1,3,4]

0, 0, 4

root = 1
root_in_index = 1

left_size = 1
right_size = 2

    1, 0, 1
        root = 2
        root_in_inde = 0
        left_size = 0
        right_size = 0
    2, 2, 2
        root=3
        root_in_index=2
        left_size = 0
        right_size = 1
"""
        
            

        