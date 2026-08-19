"""
Approach: given all ordered subsets of nums[0]..., nums[n-1], the ordered subsets of nums[0]..., nums[n]
is just duplicate with adding the last element

e.g.
[1]
[], [1]
[1, 2]
[], [2], [1], [1, 2]

Invriant: before i, we have all subsets of nums[0]...nums[i-1] without duplicates
Preservation: creating another copy of all the subsets with nums[i] make all subsets on nums[0]...nums[i]. both unique (the new copise has element i) and cover all subsets
Consequence: all subsets are found
Time and Space Complexity: 2^n --> every time you add 1 to the input you double the ooutput size which affects both time and space.
This is high time and space complxity, but len is <= 10 2^10 == 1024
Edge Cases:
empty --> [[]]

"""
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        given list of unique numbers return all subsets
        """

        subsets = [[]]

        for num in nums:
            new_subsets = [] # all the new subsets which has num as the last element
            for subset in subsets:
                new_subset = subset.copy()
                new_subset.append(num)
                new_subsets.append(new_subset)

            subsets.extend(new_subsets)

        return subsets

"""
test 
nums = [7]

subsets = []

num = 7

new_subsets = [7]

subsets = [[], [7]]

"""


        