"""
Approach: Trie. with dot at index i, means youo should explore all paths from there
Invairiant: at depth d we're at the trie where the query prefix len d-1 and the trie path d-1 mathc
Preservation: if at index d, is a letter going down the path at that letter, keeps the match for len d. if it's a dot doing down all existing letters keeps all possible matches
consequence: when d=len(word) we find if there is a match or not
time: adding word - len(word). search - withoutout dots - len(word) with dots - any dot can 26X paths --> count(dots) * len(word)
space: 26*len(max-word)

Edge Cases:
dot in the middle
dot in the end
word only exists as a prefix
dot without any children

"""
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    """ A dictionary allowing searching words and support dot wildchar
    """

    def __init__(self):
        self._trie_root = TrieNode()

    def addWord(self, word: str) -> None:
        """ Adds a word to the dictionary
            assuming the word is only made of lower case letters
        """
        current = self._trie_root
        for c in word:
            if not c in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True
        
    def search(self, word: str) -> bool:
        """ Returns if a word exists in the dictionary
            the word can contains dot wildchars
        """
        def suffix_exists(i: int, current: TrieNode) -> bool:
            # print(word, i, current.is_word, current.children)
            if i == len(word):
                return current.is_word
            
            if len(current.children) == 0 or (word[i] != '.' and word[i] not in current.children):
                return False
            

            if word[i] != '.':
                return suffix_exists(i+1, current.children[word[i]])
            else:
                for c in current.children:
                    if suffix_exists(i+1, current.children[c]):
                        return True
                return False
        
        res = suffix_exists(i=0, current=self._trie_root)
        # print(word, res)
        return res

"""
Test

"WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

b
    a
        y true
d
    a
        y true
m
    a
        y true

run:
bug 1 : positional argument after keyword
2 : trie_node instead of trie_root * 2
3: output was nne - expected return is bool - missed a flase after the loop for no match
4: say is false should be true
"""
        
