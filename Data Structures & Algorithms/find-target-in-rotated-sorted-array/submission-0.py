"""
Approach: the order is [<un-known-index>...<last>...<unknown-index>). 
if target < mid or > hi - go left. otherwise go right
Invariant: for a given hi and lo, we know that target is either between hi and lo or not in the list at all
Preservation: looking at lo, mid, and hi follow the approach, the target is either in lo, mi, or in mid,hi.
Consequence: invariant is correct for the base case 0, last, and we keep narrow it down and preserve the invariant until it's either small enough (const)
or prove taget not exit on the list (hi<lo)--> we can find the colution
Time: O(log(n)) - we cut the dimain by ~/12 each time
Space: const
edge cases:
hi=lo+2 --> mid=lo+1
hi=lo+1 --> mid=lo
hi=lo --> mid=lo
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo<hi:
            mid = (hi+lo)//2
            if target == nums[mid]:
                return mid


            if nums[mid] < nums[hi]:
                if target < nums[mid] or target > nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1
            else: #mid > hi --> hi<lo<mid
                if target <= nums[hi] or target >= nums[mid]:
                    lo = mid+1
                else: # 
                    hi = mid-1

        return lo if nums[lo] == target else -1

"""
[3,4,5,6,1,2] target 1

lo=0(3), hi=5(2), mid=2(5)

mid>hi
target<=hi --> lo = 2(5) hi=5(2) mid=3(6)
target < hi -> lo=3(6) hi=5(2) mid=4(1) -- return 4

bugs 
1. time exceeded for nums=[3,5,6,0,1,2] target 4

"""


                    
        


        