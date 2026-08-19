"""
rotten fruit is contaigous 

Approach: BFS from all rotten fruits. every time increase the ticks
Invariant: at any time the queue contain the fruits with the time 
in which they become rotten in non-decreasing order
with all unvisited fresh fruits are still not rotten in any smaller tick
preservation: when adding the current fresh neighbors 
Consequence: once queue is empty, no fresh fruits remained. 
time: O(V+E)
Space: O(V)
possible improvements: not pushing the distnace, but make it a special node

Edge case:
no rotten fruits - never - -1
all rotten fruits - 0
unreachable fresh fruits -1
"""
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time in which all fruits are rotten.
        assuming  each tick th neighbor get rotten as well
        """
        
        queue = collections.deque()
        visited = set()
        max_time = 0
        total_fruits = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    total_fruits += 1
                elif grid[i][j] == 1:
                    total_fruits += 1


        # count fresh fruits

        while queue:
            i, j, d = queue.popleft()
            max_time = d

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:

                #not legal cell
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    continue

                if grid[x][y] != 1 or (x, y) in visited:
                    continue

                queue.append((x, y, d+1))
                visited.add((x,y))

        if len(visited) == total_fruits:
            return max_time
        else:
            return -1 # not all fresh fruits are reachable




        