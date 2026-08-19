# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach: BFS on tree (Tree is a graph). pushing lefel separator right after root and everytime we encounter a separator
Invariant: Before pulling the nexe node from the queue, the results are ordered correctly level-by-level and left-to-right and a separator between levels in the queue
ans so is the queue (In particular the nodes in the queue are next level or right to the processed ones). and all unvisited nodex are either next level or right to those in the queue
Preservation: when we pull from the queue, the processed node is the enxt one in the results (Being first in the queue) and is childrent are the next ones in the queue
(the children od processed ones are already in teh queue). if we pulled a separator. we finished all the nodes of current level, so next node children are of the next level
Consequence: the fina results are ordered level by level and left to right
Time: N
Space: N for visited and result

Edge Cases:
null tree


"""
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[]]
        if root is None:
            return []

        queue = collections.deque([root, -1])
        visited = {root}

        while queue:
            current = queue.popleft()
            if current == -1:
                if queue:
                    queue.append(-1)
                    result.append([])
                continue

            result[-1].append(current.val)
            for next_node in (current.left, current.right):
                if next_node is not None and next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

        return result

"""
example 1

queue {1, -1}
visited {1}
result [[]]

1
    re = [[1]]
    q = [-1, 2, 3]
    vis = {1, 2, 3}

-1
    q = [2, 3, -1]
    res = [[1], []]

2
    q = [3, -1, 4, 5]
    res = [[1], [2]]

3 
    q = [-1, 4, 5, 6, 7]
    res = [[1], [2,3]]
-1
    q = [4,5,6,7,-1]
    res = [[1], [2,3], []]
 
 4, 5, 6, 7

    q = [-1]
    res = [[1], [2,3], [4,5,6,7]]

-1
    q = []
    res same


"""


            



        
        