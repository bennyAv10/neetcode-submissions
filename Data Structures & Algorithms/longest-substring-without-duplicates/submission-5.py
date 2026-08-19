"""
hold a dictionary where the location of each charater

whenever encounter duplication - we should put left pointer on the new one and remove all the pointers to earlier locations
"""
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring with all charaters unique
        """
        if not s:
            return 0
        l = 0
        loc_dict = {s[0]: 0}
        max_len = 1
        for r in range(1, len(s)):
            if s[r] in loc_dict:
                current_len = r-l
                max_len = max(max_len,current_len)
                l = loc_dict[s[r]]+1
                loc_dict = {k: v for k, v in loc_dict.items() if v >=l}

            loc_dict[s[r]] = r

        max_len = max(len(s)- l, max_len)

        return max_len 
        


        