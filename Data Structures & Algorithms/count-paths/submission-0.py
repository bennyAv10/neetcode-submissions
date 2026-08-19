"""
Approach: bottom-up DP. stars with the last cell (bottom-right) which is one. then feel row by row. each cell is a combination of the cell to the right and to the bottom
Alternatives: any path is (m-1) steps down and n-1 steps right. you can pick one (eitehr right or down) - so it's m-1 choose k-1 == (m-1)! /((n-1)!*((m-1)-(n-1))!) 
Invariant: before procesing cell i, j we know the count for x, y where x > i or x=i and y>j
Preservation: to go from i,j to th the bottom right, you mus go eitehr through i+1, j or i, j+1. now, before processing the rest or the row the invariant stands for i, j-1.
if i, j is the last row, the invariant stays for i-1, last
Consequence: we know for i,j=bottom-right the count is one and the invariant stands tehreafter
Time: M*N
Space: M*N
Edge cases:
m=n=1 (0 is excluded)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Give a board of m rows and n columns returns the number of unique paths got go from the top left cell to the bottom rght cell
        Assuming only right and down steps are allowed
        """
        unique_paths = [[0]*n]*m

        # init last row - all one yoou can only go right
        unique_paths[m-1] = [1]*n

        for i in range(m-2,  -1, -1):
            # last column is alway one - you can only go down
            unique_paths[i][n-1] = 1
            for j in range(n-2, -1, -1):
                unique_paths[i][j] = unique_paths[i+1][j] + unique_paths[i][j+1]

        return unique_paths[0][0]

"""
test:
Input: m = 3, n = 6

up = 000

last row = 1, .., 1
last column also 1

1,4
1+1=2
1,3
1+2=3
1,2
1+3=4
1,1
1+4=5
1,0
1+5=6
0,4
1+2=3
0,3
3+3=6
0,2
6+4=10
0,1
10+5=15
0,0
15+6=21

bugs:
1. init last row to [1*n] instead of [1]*n - took me 5 minutes or pdebug print to figure that out :-(

total time: 40 minutes


"""
        