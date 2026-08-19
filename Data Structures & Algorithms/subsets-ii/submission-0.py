"""
the output starts with empty list. then, for every num, you get over each surrent subset and you clone it and add nums to one
Invariant: before processing nums[i] the output contain all subsets of nums[0..i]. 
preservation: addignums[i] means all the existing subsets + vriant for each one with nums[i] incldued
Consequence: it's true for i=0 (empty subset)
Time: 2^n - for every step, you double the number of subsets for N iterations. input constrains is n<=11 so 2^n is still ok
Space: 2^N for the output

"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Returns the power set of nums - all possible subsets
        """
        output = set()
        output.add(tuple())

        for num in nums:
            new_subsets = set()
            for subset in output:
                new_subset = subset+(num,)          
                new_subsets.add(tuple(sorted(new_subset)))
            output.update(new_subsets)

        return list(output)

"""
[1,2,1]

o=[[]]

1
o=[[],[1]]

2
o=[[],[1],[2],[1,2]]

1
o=[[],[1],[2],[1,2], [1,1], [2,1], [1,2,1]]

bug 1: created utput as a set for dedup, but 
bug 2: 1,2 and 2,1 are duplicate
"""
        