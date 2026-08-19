"""
sort each string and use a s the map key. the value is the list of originals trings

K lex of amx strings
N number of strings

spac comlexity O(NK)

time O(KlogkN)

solution 2
graph starts with empty, and depth K

Time KN

"""

def _getKey(item: str) -> str:
    """Generate the map key."""
    return "".join(sorted(item))

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_by_key = defaultdict(list)
        for item in strs:
            key = _getKey(item)
            anagrams_by_key[key].append(item)

        return list(anagrams_by_key.values())


        