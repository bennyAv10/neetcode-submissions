class Solution:
    """
    a dict from str to list[str]
    the key is teh sorted string
    create a default dict
    and use.sort
    in the end just return the values of teh dict
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list[str])
        for s in strs:
            anagrams_map[''.join(sorted(s))].append(s)
        # print(anagrams_map)
        return list(anagrams_map.values())