"""
for any (i, j) calculate the sub array and keep the max --> N^3
if you optimize with prefix it's only N^2 for a given i, j the sum(i, j) = sum(i, j-1) + j

per j - the max subarray ending at j --> it's either max ending at j-1+j or j alone
now we keep tracking of max_so_far

Approach: iterate tracking max so far and max ending at this element 
Invariant: at element at element j assuming we know max_so_far and max ending at j-1. 
max_ending at j is either max ending at j-1 + j itself or just j.
Time: O(N)
Space: O(1)

edge cases:
empty - assumed noot

all negative - handled by init maxes to first element
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ Returns the max sub of any continuous sub array

        Args:
            Nums: array of integers. unsorted. any integer
        """

        max_ending_at_i = nums[0] #len >=1
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_at_i = max(max_ending_at_i+nums[i], nums[i])

            max_so_far = max(max_so_far, max_ending_at_i)

        return max_so_far

        