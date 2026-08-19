"""
edge cases:
invalid value (not 1-9 or .) --> throw error
size -> throw an error

define 
check row --> called for 0-8
check col --> called for 0-8
check square --> called for 0-3

each will have a set

a bit of duplicate logic, but code is mor readable

time complexity (N=matrix dimension - 9): N^2 *3 - each of row, col, and sqares validation is N^2
"""
valid_values = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
class Solution:
    
    def isValidRow(self, board: List[List[str]], row: int) -> bool:
        visited = set()
        if len(board[row]) != 9:
            raise ValueError(f"row {i} has len {len(board[row])} != 9")

        for c in board[row]:
            if c not in valid_values:
                raise ValueError(f"{c} is invalid")
            if c != "." and c in visited:
                return False
            visited.add(c)
        
        return True

    def isValidColumn(self, board: List[List[str]], col: int) -> bool:
        visited = set()
        for i in range(9):
            c = board[i][col]
            if c not in valid_values:
                raise ValueError(f"{c} is invalid")
            if c != "." and c in visited:
                return False
            visited.add(c)
        
        return True

    def isValidSquare(self, board: List[List[str]], square: int) -> bool:
        visited = set()
        
        square_i = square//3
        square_j = square%3
        for i in range(square_i*3, square_i*3+3):            
            for j in range(square_j*3, square_j*3+3):
                val = board[i][j]
                if val not in valid_values:
                    raise ValueError(f"invalid value {val} in {i} {j}")
                if val != "." and val in visited:
                    return False
                visited.add(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board, i):
                return False
            if not self.isValidColumn(board, i):
                return False
            if not self.isValidSquare(board, i):
                return False
        
            
        
        return True
        