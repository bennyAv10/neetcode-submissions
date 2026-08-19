"""
Approach: starts from each place in the board and build words with <= 10 length. next, find the words in he dictionary

building the trie: back tracking. once reaching length f ten you fold back. you keep adding to trie as you go
search word: find if in the trie
Invariant: with backtracking at given depth you have prefix of length i-1
Preservation: you have all decandants prefixes of size i

Time: Building the trie. N(rows count) * M (column count) * 10 (max word len). filtering: K (count words) * 10
Space: N*M*10
"""
class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        given a board of letters, return all the words from the given list that could be built from the board
        """
        def visit(i: int, j: int, current: TrieNode, depth: int, visited: set):
            visited.add((i, j))
            if not board[i][j] in current.children:
                current.children[board[i][j]] = TrieNode()
            
            if depth < 9:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if x<0 or y<0 or x>= len(board) or y >=len(board[x]) or (x,y) in visited:
                        continue
                    visit(x, y, current.children[board[i][j]], depth+1, visited)
            visited.remove((i,j))
        
        root = TrieNode()

        for i in range(len(board)):
            for j in range(len(board[i])):
                visit(i, j, root, 0, set())

        def word_exists(word: str):
            current = root
            for c in word:
                if not c in current.children:
                    return False
                current = current.children[c]

            return True


        return [word for word in words if word_exists(word)]


        