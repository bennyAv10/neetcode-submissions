"""
tree is connected graph without cycles
Approach: if num edged != n-1 there is a cycle. DSU - keep connecting components. if cycle is fund it's not a tree. if tehre is more than a single components it's not a tree(not connected)
Alternatives: build graph and run BFS and make sure all nodes are visited. time - O(V+E). space. O(E) - similar to DSU, btu we want to practice DSU
Invariant: before processing edge i. we have connected components derived from edges: 0, ..., i-1 and there is no cycles
Preservation: processing edge i conencting x, y. if x and y are already in the same components - it's a cycle. if not, we connect two componenets - now
after processing edge i we have the connected graph by edges 0, ..., i
Consequence: since invariant it's true for i=0 (no edges), eventually we either find cycle or it's a tree
Time: O(E)
Space: O(E)
Edge cases:
no nodes or edges - excluded
self cycle - should take into account
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Returns True if the graph with `n` nodes and the given edges is a valid tree

        A valid tree is defined as connected graph without cycles
        """
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
                parent = node_to_ancestor[x]
                node_to_ancestor[x] = root
                current = parent
            
            return root
        
        def size(x: int) -> int:
            x = find_root(x)
            return root_to_size[x]

        def union(x: int, y: int) -> bool:
            """
            if already connected (cycle) return False
            Otherwise, connect and return True
            """
            x = find_root(x)
            y = find_root(y)

            if x == y:
                # cycle
                return False
            if size(y) > size(x):
                x,y = y,x
            
            node_to_ancestor[y] = x
            root_to_size[x] += root_to_size[y]
            del root_to_size[y]

            return True

        if len(edges) != n-1:
            # tree has exactly n-1 edges
            return False

        for x, y in edges:
            if not union(x, y):
                return False

        return True
"""
test
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

edges == n-1 


0,1

1 ->0
0->0

0,2

1->0
0->0
2->0

0,3
3->0
sies

bugs:

1. forgot to call find_root from size first
2. mistkenly put in union nodex_toncestor[x]=x

"""
        