class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(i: int) -> bool:
            nums = set()
            for j in range(len(board)):
                num = board[i][j]
                if num != '.':
                    if num in nums:
                        return False
                    nums.add(num)
            
            return True

        def check_col(j: int) -> bool:
            nums = set()
            for i in range(len(board)):
                num = board[i][j]
                if num != '.':
                    if num in nums:
                        return False
                    nums.add(num)
            return True

        def check_box(row_start: int, col_start: int) -> bool:
            nums = set()
            for i in range(row_start, row_start+3):
                for j in range(col_start, col_start+3):
                    num = board[i][j] 
                    if num != '.':
                        if num in nums:
                            return False
                        nums.add(num)
            return True
        
        for i in range(len(board)):
            if not check_row(i):
                return False
        
        for j in range(len(board)):
            if not check_col(j):
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not check_box(i, j):
                    return False

        return True 

