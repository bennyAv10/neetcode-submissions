
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or (i,j) in visited:
                    continue

                islands_count += 1
                visited.add((i,j))

                # bfs dequeue all 1
                queue = collections.deque([(i,j)])
                print(queue)

                while queue:
                    x,y = queue.popleft()

                    for c_i, c_j in ((x-1, y), (x+1, y), (x, y-1), (x,y+1)):
                        if c_i < 0 or c_i >= len(grid) or c_j < 0 or c_j >= len(grid[0]) or (c_i, c_j) in visited or grid[c_i][c_j] == "0":
                            continue
                        
                        visited.add((c_i, c_j))
                        queue.append((c_i, c_j))


        return islands_count

"""
test with example 2

i, j =0 0

island_count = 1

x, y = 0 0 
 loop n 1,0 0,1


"""
            
        