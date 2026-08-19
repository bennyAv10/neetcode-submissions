"""
edge cases
empty input --> empty output
empty string is valid
duplicates

solution hash table with list
the key is the sorted (canonical) representation of the anagram

once done adding all the strings to the dict, go over the dict values and each value (which is a list) to the response list
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for s in strs:
            canonical_anagram = "".join(sorted(s))
            anagrams_map[canonical_anagram].append(s)

        res = []
        for anagrams_family in anagrams_map.values():
            res.append(anagrams_family)

        return res


"""
Manual testing

[]

res = []

[""]
map = {"":[""]}
"""
        