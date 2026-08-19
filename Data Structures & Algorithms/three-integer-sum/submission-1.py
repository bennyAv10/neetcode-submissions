"""
naive approach - N^3 for each i, j find k 

2.
sort the array (nlogn)

for each element rum two pointers algorithm - N^2

3.
create a dict with the all the elements val->index
go over every possible pair of th elist and find if -(a[i]+a[j]) is in the 

2 vs 3 - 2 needs sorting which could be considered as apsace if we should preserve the original order

Approach: Sort the list and for each i apply tw-sums approach for the elements [i+1, ..., last]
invariant: for a give i we find all possible two sums starting at i+1
invariant for two sum: 
if l+r < target --> any two sum can only be in l+1, r
if l+r > target --> any two sum can only be in l, r-1
if l+r==target -->
    1. l, r - is correct answer
    2. l+1, r can also be a good answer (assuming l+1 == l)
    3. l, r-1 can also be a good answer
    4. there might be another good answer somewhere deeper

    we need to count how many equal l and how many equal r e.g. equal l's 2 and equal r's 3 --> we have 6, so we can return 6 same
    then keep iterating with for next l and r

bug 1 (found on run) 

[-4, -1, -1, 0, 1, 2]

-1
[-1, 2]
[0,1]

-1
[0, 1]

I missed the duplicate triples rule
"""
class Solution:
    def twoSum(self, nums: List[int], start_index: int, last_index: int, target: num) -> list[tuple[int]]:
        """
        Returns all the two elements from a sorted list which adds up to the given target.
        The searched range is start_index to last_index
        if no such elements exist, return None 
        """
        l = start_index
        r = last_index

        result = []

        while l<r:
            l_val = nums[l]
            r_val = nums[r]
            candidate = l_val + r_val
            if candidate == target:
                result.append((l_val, r_val))
                
                if l+1 < r and nums[l+1] == l_val:
                    l+=1
                else:
                    r-=1
            elif candidate < target:
                l+=1
            else: # candidate > target
                r -= 1
        
        return result
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()

        for i in range(len(nums)):
            current_two_sums = self.twoSum(nums, i+1, len(nums)-1, -1*nums[i])

            for twoSum in current_two_sums:
                result.add((nums[i], twoSum[0], twoSum[1]))

        return list(result)

        