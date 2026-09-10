"""
constrains: 100k --> NlogN is still fine, but not N^2

Approach: sliding window tracking longest. we keep track on letters count and max letter

right move - we update the count of the new leeter and check if it's the maxx. if count of all other letters is smaller than k window is valid - we should check if it's the new max
if windo isn't valid we start moving left pointer until it's valid again

time: N
Space: 1

edge cases:

k=0
len(s) = 1
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0

        max_sub=1
        max_char=s[0]
        window_count = collections.defaultdict(int)
        window_count[s[0]]+=1

        while right < len(s):
            
            # is window valid
            win_len = right-left+1
            is_valid = win_len-window_count[max_char]<=k
            
        
            # check max
            if is_valid:
                if win_len>max_sub:
                    max_sub=win_len

                # move right pointer
                if right+1<len(s):
                    right+=1
                    window_count[s[right]]+=1
                    if window_count[s[right]] > window_count[max_char]:
                        max_char = s[right]
                else: 
                    break
            #else window not valid
            else: 
            # move left pointer
                window_count[s[left]]-=1
                if max_char == s[left]:
                    for c in window_count:
                        if window_count[c]>window_count[max_char]:
                            max_char=c
                left+=1
        
        return max_sub

"""
 "AAABABB", k = 1


r=0,l=0
ms=1
mc=A

wc={"A": 1}

1
right=1
wc={"a":2}

2

"""


       


        