"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Approach: BFS on graph. unvisited nodes are copied. any edge is copied (You stop traversing in visited nodes - no edge is visited twice)
Invariant: when visiting node  (Through an edge) the source node is first time --> edge is first time. dest node is either already visited - only nede to copy the edge
or first time need to create both. 
Time: N+M (visiting all nodes and walk through all edges)
Space: O(N) the visited
DFS vs BFD: same time and space complexity
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = Node(val=node.val)

        origin_to_copy = {node: clone}
        stack = collections.deque([node])

        while stack:
            current = stack.popleft()
            
            for origin_neighbor in current.neighbors:
                if not origin_neighbor in origin_to_copy:
                    stack.append(origin_neighbor)
                    origin_to_copy[origin_neighbor] = Node(val=origin_neighbor.val)

                current_copy = origin_to_copy[current]
                neighbor_copy = origin_to_copy[origin_neighbor]

                current_copy.neighbors.append(neighbor_copy)
                # neighbor_copy.neighbors.append(current_copy)

        return clone

        


        