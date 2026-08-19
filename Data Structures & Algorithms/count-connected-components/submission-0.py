"""
Approach: Using DSU connect nodes using edges. in the end count number of roots + all the isolated nodes
Invariant: before processing edge i, all the connected components by edges 0, ..., i-1 are correct
Preservation: the edge is iether a cycle or connect two components - this is done correctly by DSU and now the assumption is correct for 0, ..., i
Time: O(E) - (no V becuaseu we only iterate over edges)
Space: O(E)
Edge cases:
no nods or no edges - excluded. self cycle excluded
nodes without edges
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_ancestor = {}
        root_to_size = {}

        def find_root(x: int) -> int:
            if not x in node_to_ancestor:
                node_to_ancestor[x] = x
                root_to_size[x] = 1
            
            current = x
            while node_to_ancestor[current] != current:
                current = node_to_ancestor[current]

            root = current

            current = x
            while current != root:
                parent = node_to_ancestor[current]
                node_to_ancestor[current] = root
                current = parent
            
            return root

        def size(x: int) -> int:
            x = find_root(x)
            return root_to_size[x]
        
        def union(x: int, y: int) -> None:
            x = find_root(x)
            y = find_root(y)

            if x != y:
                if size(x) < size(y):
                    x,y = y,x
                node_to_ancestor[y] = x
                root_to_size[x] += root_to_size[y]
                del root_to_size[y]
        
        for x, y in edges:
            union(x, y)

        components = len(root_to_size)
        connected_nodes = sum(root_to_size.values())

        return components +(n - connected_nodes)

"""
n = 5, edges = [[0,1],[1,2],[3,4]]

0,1

    1 -> 0
    0 -> 0

    s: 0:2

1,2
    1 -> 0
    0 -> 0
    2-> 0

    s: 0:3
3, 4
    1 ->0
    0 -> 0
    2 -> 0
    3 -> 3
    4 -> 3

    s: 0:3, 3: 2

components: 2
size: 5 --> 2


"""
        