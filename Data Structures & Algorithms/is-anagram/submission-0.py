class Solution:
    """
    1. iterate with two pointers: forward and backward
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        for c in s:
            s_map[c]+=1
        
        for c in t:
            if c not in s_map:
                return False
            s_map[c]-=1
            if s_map[c]<0:
                return False
        
        return True


        