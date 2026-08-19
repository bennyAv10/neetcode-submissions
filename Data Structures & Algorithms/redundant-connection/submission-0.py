"""
Approach: Using DSU (Disjoined Set Union) algorithm, scan the edges from left to right and with edge x, y union x and y.
if x and y are alredy in the same set we found the extra edge
Invariant: Before processing and Ith edge we have all the connected componentes according to the edges 0, ..., i-1
Preservation: After processing Ith edge (x, y). x and y are either already connected (extra edge is found) or with DSU we just connected X and Y components.
Now we have all the connected components accoding to the edges 0, ... ,i
Consequence: since all nodes are connected and there is exactly one extra node creating cycle we'll find this extra edge
Time: in DSU, all operations are almost one, so it's linear to number of nodes (Or edges which are exectly V+1 here)
Space: O(N) - DSU holds all connected nodes in memory
Edge cases:
self cycles aer excluded
zero edges or nodes are excluded
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Given a list of edges in undirected graph, find the first edge creating cycle.
        returns empty list if no cycle is detected
        """
        node_to_ancestor = {}
        root_to_size = {}

        def find_root(x: int):
            if not x in node_to_ancestor:
                # root is indicated by self parenting
                node_to_ancestor[x] = x
                root_to_size[x] = 1

            current = x
            while node_to_ancestor[current] != current:
                current = node_to_ancestor[current]

            root=current
            current = x
            while current != root:
                parent = node_to_ancestor[current]
                node_to_ancestor[current] = root
                current = parent
            
            return root
        
        def size(x: int):
            x = find_root(x)
            return root_to_size[x]

        def union(x: int, y: int):
            x = find_root(x)
            y = find_root(y)

            if x != y:
                if size(y) > size(x):
                    x, y = y, x
                node_to_ancestor[y] = x
                root_to_size[x] += root_to_size[y]
                del root_to_size[y]

        
        for (x, y) in edges:
            if find_root(x) == find_root(y):
                return [x, y]
            else:
                union(x, y)

        return []
"""
Input: edges = [[1,2],[1,3],[3,4],[2,4]]

1, 2

1 -> 1
2 -> 1

s:
1 --> 2

1, 3

1 --> 1
2 --> 1
3 --> 1
s:
1 --> 3

3, 4

1, 2, 3, 4, --> 1
s: 1--> 4

2, 4

2 --> 1
4 --> 1

--> 2, 4

bug 1: returns [1,1] --> I returned the root of the cycle edge
"""
        