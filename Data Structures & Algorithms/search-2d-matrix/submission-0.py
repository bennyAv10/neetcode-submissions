"""
binary search - just return if it's there or not

assumption: all rows of the same size
treat the 2d like one long 1d matrix[i] == matrix[i//len(matrix[0])][i%len(metrix[0])]

invariant: if target exist its in [l, r]
when an elment m in [l...r] is smaller than target we can make the new l as m+1. similar for bigger

alternative: two level search one to find the row l = r-1 - same time complexity, but I consider translation layer simpler,
although there is an extra cost of calculating floor and modulo

time(Olog(N*M)) with N row count and M column count

"""
class Solution:

    def getAsOneD(self, matrix: List[List[int]], i: int) -> int:
        """Get the element i in the matrix if it was 1d array"""
        num_cols = len(matrix[0])

        row = i//num_cols
        col = i%num_cols

        return matrix[row][col]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Search sorted matrix where each row is sorted and the first element in each row is 
        greater or equal than the last element in the previous row"""

        M = len(matrix)
        N = len(matrix[0])

        l = 0
        r = (N*M)-1

        while l<=r:
            mid = (l+r)//2

            mid_elem = self.getAsOneD(matrix, mid)
            if mid_elem == target:
                return True
            elif mid_elem < target:
                l = mid + 1
            else: # mid_elem > target
                r = mid - 1

        return False
    
        