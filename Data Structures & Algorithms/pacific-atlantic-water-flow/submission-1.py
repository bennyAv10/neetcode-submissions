"""
all cells at the border can stream water to the nearby ocean

Approach: start BFS from all sources from pacific you can connect to higher cell.
same BFS from atlantic sources - the overlapping is the true
Invariant: visited and queue only contain nodes that can stream water to the current ocean.
Preservation: We add neighbors IIF they higher from current node --> can stream to current node --> can stream to ocean 
Time: O(V+E)
Space: O(V)
Edge cases:
small size
unreachable cells

Possible optimization:
1. delegate BFS to a function avoid coe duplication
2. only start from pacific visited with reversed connection logic - optimizing time but not asymptotically
3. starting from bottom left and top right corners is a jocker you can boths oceans from a single source
"""
import collections

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Returns list of coordinate pairs on nodes in heights from which 
        water can flow to both the atlantic and pacific oceans
        """
        pacific_visited = set()
        queue = collections.deque()

        # 1. Add all pacific neighbors - non-negative mwater can flow 
        for i in range(len(heights)):
            queue.append((i, 0))
            pacific_visited.add((i, 0))

        for i in range(len(heights[0])):
            queue.append((0, i))
            pacific_visited.add((0, i))

        # 2. find all nodes frm which water can flow to the pacific
        while queue:
            i, j = queue.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x < 0 or y<0 or x>= len(heights) or y >= len(heights[0]):
                    continue
                if (x, y) in pacific_visited:
                    continue
                
                if heights[x][y] >= heights[i][j]:
                    queue.append((x, y))
                    pacific_visited.add((x,y))

    
        atlantic_visited = set()
        # 3. add all atlantic sources
        for i in range(len(heights)):
            queue.append((i, len(heights[0])-1))
            atlantic_visited.add((i, len(heights[0])-1))

        for i in range(len(heights[0])):
            queue.append((len(heights)-1, i))
            atlantic_visited.add((len(heights)-1, i))

        
        # 4. find all cells from which water can flow to the atlantic
        while queue:
            i, j = queue.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x < 0 or y<0 or x>= len(heights) or y >= len(heights[0]):
                    continue
                if (x, y) in atlantic_visited:
                    continue
                if heights[x][y] >= heights[i][j]:
                    # water can flow from x, y to i, j whichi is already connected
                    queue.append((x, y))
                    atlantic_visited.add((x,y))
        # print("pacific: ", pacific_visited, " atlantic: ", atlantic_visited)
        #5. return the overlap
        return list(atlantic_visited & pacific_visited)