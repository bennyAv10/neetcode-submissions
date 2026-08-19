"""
Approach: DP. the min cost for i,j is the min of i+1,j and i, j+1 + cost of i,j itself
Invariant: before processing i,j, we know the min cost for any x,y where either x>i or x=i and y>j
Preservation: the min cost as stated in the approach correctly determine the cost for i,j --> now for i, j-1 invariant stands.
when completeing the row, it stand for i-1
Consequence: the base line is bottom right. with invariant and preservation we know the cost for 0,0
Time: O(M*N)
Space: O(N)
Alternative: Djakstra as a graph. but it'll be more expensive
Edge cases:
last row - only right
last col - only below
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cost = [grid[-1][j] for j in range(m)]

        for j in range(m-2, -1, -1):
            cost[j] += cost[j+1]

        for i in range(n-2, -1, -1):
            cost[-1] += grid[i][-1]

            for j in range(m-2, -1, -1):
                cost[j] = min(cost[j], cost[j+1])
                cost[j] += grid[i][j]
        
        return cost[0]

"""
test:
[1,2,0],
[5,4,2],
[1,1,3]

c = [1,1,3]
c=[5,4,3]

i = 1
    c = [5,4,5]
    j=1
    c = [5,8,5]
    j=0
    c=[10,8,5]
i=0
    c=[10,8,5]
    j=1
    c=[10,7,5]
    j=0
    c=[8,7,5]
"""

        