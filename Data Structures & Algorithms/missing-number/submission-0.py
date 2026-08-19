"""
Approaches:
1. sort in nlogn (or bucket sort in N but space log(N)) and go over numbers
2. heapify in N then popping until skipping a number - NlogN
3. xor [1,...,n] and xor all nums in nums. then xor them together
4. sum of arithmetic series is (s1+sn)/2 

chosen approach - #3 one of the more efficient ones + I'm practicing bitwise operators
Invariant/preservation/adersarial cases not relevant here. only that X^X=0
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all_nums=0        
        for i in range(len(nums)):
            xor_all_nums ^= i
            xor_all_nums ^= nums[i]

        xor_all_nums ^= len(nums)
        return xor_all_nums

        
        