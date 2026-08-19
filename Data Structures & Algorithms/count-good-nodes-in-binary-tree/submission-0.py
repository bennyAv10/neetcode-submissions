# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: pass the max value from the upper stream (-101 init). 
for None return 0. otherwise return the sum of good nodes in left and right + 1 if current node is bigger than max
Time: O(N) with N = nodes count
Space: O(H) with worst case H~=N
Invariant: 2 actually: 1. when node x is called we know the max value from ancestrs 2. when the call from X decandas is back we know number of good nodes in each sub tree
Preservation: 1. if if we know max value from root down to x, then for x children the value is max(max, x.vaL) 2. since we know num of good nodes in each subtree and we can tell if x itself is a good node when done with x 
the invariants hold for x parent
Consequence: invariant 1 base case is the root (max is -101) and 2 base case the the none leaves
"""
class Solution:
    def goodNodes(self, root: TreeNode, max_val=-101) -> int:
        """
        return the number of good nodes in the tree

        A goof node is one whose value is greater or equal to all nodes all the way up to the root
        """
        if root is None:
            return 0
        
        am_i_good = root.val >= max_val
        
        max_val=max(root.val, max_val)
        left_goods = self.goodNodes(root.left, max_val)
        right_goods = self.goodNodes(root.right, max_val)

        return left_goods + right_goods + (1 if am_i_good else 0)

"""
2,1,1,3,null,1,5

2
am=1
mx =2
    1
        am=0
        3
            am=1
            -->1 
        -->1
    1
        am=0
        1
        am=0
        -->0
        5
        am=1
        -->1
    -->1
-->3

adverserial:
empty tree - excluded

"""