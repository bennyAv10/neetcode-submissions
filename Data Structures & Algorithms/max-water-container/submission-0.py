"""
naive approach: N^2 you check all other bars for each bar




Approach: two pointers, we check current capacity > max. in any case we move the lower of l, r one step closer. we stop when l=r
Invariant: Assuming we have current max from earlier bars or current pair, the only reason to go narrower, is to find higher container.
which it's better narrowing from the lower side. if next bar is lower or same - capacity is smaller - if it's higher the capacity might be bigger
time complexity: linear - wth iteration we move once
Edge cases: 
empty - assume not 
single bar - assume not
all bars are 0
emulating witht he given example:

[1,7,2,5,4,7,3,6]
max=0

l=0, r=7
capacity= 7*1=7 -->max

l=1, r=7
6*6=36 --> max

l=1, r=6
3*6 = 18

no need to finish emulation
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_capacity = 0

        while l < r:
            current_height = min(heights[l], heights[r])
            current_capacity = (r-l) * current_height
            max_capacity = max(current_capacity, max_capacity)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        
        return max_capacity
        