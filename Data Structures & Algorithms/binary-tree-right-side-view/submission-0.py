# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: BFS with level separator. start with right child always. at each level you add the first node to the results
Invariant: result are the processed levels so far. queue is from right to left with level seperator. with 0-2 level at any given time
Preservation: processing a separator means we processed all nodes of the n-1 level -> all n level nodes are in the queue --> putting seprator sill distinguish n and n+1.
processing a standard node goes to the results IIF it's the first one for that level
Time: O(N)
Space: width (queue) + height (result) which is worst case is O(N)
Edge cases:
none
"""
_LEVEL_SEPARATOR = -1
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the tree nodes which are visible from the right (Right-most nodes at each level), ordered from top to bottom
        """
        if root is None:
            return []

        result = [root.val]
        queue = collections.deque([root, _LEVEL_SEPARATOR])

        while queue:
            node_or_separator = queue.popleft()
            if node_or_separator == _LEVEL_SEPARATOR:
                if not queue:
                    break
                queue.append(_LEVEL_SEPARATOR)
                node_or_separator = queue.popleft()
                result.append(node_or_separator.val)

            node = node_or_separator

            for next_node in node.right, node.left:
                if next_node is not None:
                    queue.append(next_node)

        return result

"""
test example 1

res = [1]
queue = [1, -1]

1
    queue = [-1, 3, 2]

-1
    q = [3, 2, -1]
    3
    res = [1, 3]
    q = [2, -1]
    q = [2, -1, 5]
2
    q = [-1, 5, 4]

-1
    5
    q = [4, -1]
    res = [1, 3, 5]

4

-1
    q = []




"""

        