"""
Naive Approach: all possible combinaitons in the length of `word`.
Naive time complexity N*M*4^len(word) (you start with every cell and keep extending 4 directions)

Approach: DFS with backtracking. start with every cell containing the word first letter.
You can revisit cell, just not on visiting path.
you only visit neighbors with the expected next character

Invariant: the visiting cells contains a prefix of the word of size k.
Preservation: looking at the at the neighbors which are not on the visiting path which
contain the k+1 letter from word and adding it to visiting make the visiting k+1 prefix
Consequence: at depth len(word) the prefix == word
Time: worst case - most combinations are almost correct(only last character not matched). so 
asymptotically can still be the same. but average case is much better (assuming random distribution
most combinations are ptuend on first letter)

"""
class Solution:
    def dfs(self, board: List[List[str]], word: str, i: int, j: int, prefix_indices: set[tuple[int, int]]) -> bool:
        """
        with `word` prefix of size len(prefix_indices) at prefix_indices, can we continue the word 
        all the way
        """
        prefix_indices.add((i,j))
        if len(prefix_indices) == len(word):
            return True

        
        expected_char = word[len(prefix_indices)]
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                continue
            if (x, y) in prefix_indices:
                # alerady been there
                continue
            if board[x][y] != expected_char:
                continue
            
            if self.dfs(board, word, x, y, prefix_indices):
                return True

        prefix_indices.remove((i,j))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        does the word exist in the board
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, set()):
                        return True

        return False

"""
example 1

starting dfs in 0, 2
prefix = {C}
expected_char='A'
    dfs 1, 2
    prefix = {CA}
    expected_char = T
    dfs = 1, 3
        prefx {CAT} --> len = len of word

starting dfs in 2, 1

running:
error 1 - named grid instead of board
error 2 - index out of range. root cuase - i put and instead of or in the index valid check - stupid miatake because i started 
with checking a valid case and switch to excluding invalid case
error 3: 
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="SEE"
root cause: my top level func internal loop iterate over len of board intead of len board[0]

"""
        