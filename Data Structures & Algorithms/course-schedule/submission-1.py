"""
Approach: model as a graph. [a,b] is edge. can't finish IIF there is a cycle. detect a cycle by DFS if it's in the path.
we use stack (push and pop from the right)+ two sets: visiting and visited
when poping from stack first time - we put in visiting set and keep pushing children
when poping 2nd time we done visit
Invariant: when walking on a new edge [a, b] if b is unvisited - b has no prerequisites. if b visited - if it was visited 
last by [c,b] it's not on this path. if it was [b, c] - if it's nt in this path - no cycle 
Time: O(E) (You only walk through edges)
Space: O(E) - each node with an edge can be either on visiting or visited or no where

testing example
[[0,1], [1,0]]

visited={}
visiting={}
stack={0}

visiting = {0,}
stack = {0, 1}

visiting = {0, 1}
stack = {0, 1}

-->1, 0

"""
class Solution:
    def visit(self, node: int, visiting: set[int]) -> bool:
        visiting.add(node)
        for neighbor in self.graph.get(node, []):
            # print("node:", node, " neighbor:", neighbor)
            if neighbor in visiting:
                # Cycle detected [neighbor, ..., node, neighbor]
                return False
            if neighbor in self.visited:
                continue
            if not self.visit(neighbor, visiting):
                return False
        
        visiting.remove(node)
        self.visited.add(node)
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Can finish courses 0, ..., numCourses given the prerequisited (Dependencies)
        """
        if not prerequisites:
            return True # no prerequisites
        
        self.graph = defaultdict(list)
        for pair in prerequisites:
            self.graph[pair[0]]. append(pair[1])
        # print(self.graph)
        self.visited = set()
        
        for node in self.graph:
            if not self.visit(node, set()):
                return False
        return True
        

            

        