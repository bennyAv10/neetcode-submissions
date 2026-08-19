"""
distinct integers sorted - find the target in LogN or return -1

text book question - binary search

keep l and r as search domain --> target if exists is there
 check the middle between l and r

 if m is the target --> found
 if m < target --> target is m, ..., r --> set l to m+1
 if m > target --> set r to m -1

 you stop when r<l

 since you always cut the domain search by half it's O(logN))

 had 1 bug checking the loop for l<r instead of l<=r
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2

            candidate = nums[m]

            if candidate == target:
                return m
            elif candidate < target:
                l = m+1
            else: # candidate > target
                r = m-1
        
        # target wasn't found
        return -1

"""
micro test on loop

l=0, r 2
m = 1

l = 0, r=1
m = 0

l = 0 r = 0
m = 0

"""

            
        