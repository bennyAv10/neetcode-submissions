
from dataclasses import dataclass

@dataclass
class TrieNode:
    is_word: bool = False
    children = None

class PrefixTree:

    def __init__(self):
        self._root = TrieNode()
        

    def insert(self, word: str) -> None:
        """ Inserts a new word to the Trie.
        """
        current = self._root
        for c in word:
            if current.children is None:
                current.children = {}
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True


    def _find_leaf(self, s: str) -> TrieNode | None:
        current = self._root
        for c in s:
            #print(f"s: {s} c: {s} children: {current.children}")
            if current.children is None or not c in current.children:
                return None
            current = current.children[c]
        
        return current
    
    def search(self, word: str) -> bool:
        """ Returns true IIF the word exists in the Trie.
        """
        last_node = self._find_leaf(word)
        return last_node is not None and last_node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """ Returns trie IIF a word with the given prefix exists in the trie
        """
        return self._find_leaf(prefix) is not None
        
        
"""
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

init

insert dog

d
    o
        g, true

search dog
    true

search do
    false (leaf exist but not true)

errors while running 
1. dataclass annotation
2. default dict with value TrieNode
3. startwith call without any insert
"""