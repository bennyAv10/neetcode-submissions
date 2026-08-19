"""
Approach: at each  element you add yourself to the path and recusrsively visit each of the later elements 
Invariant: the particular call from i to j the path is a unique prefix of all subsets with the current path
Preservation: adding j to the path make add a unique path with i and j . in particular, this prefix is one of the subsets
consequence: all subsets are uniquely included
Time: number of subsets is 2^n (Each element can either be ther or not) and for each subset you might visit N element so 2^N * N
Space: same as time
"""
class Solution:
    def subsetsOfPath(self, nums: list[int], i: int, path: list[int], subsets: list[list[int]]) -> None:
        path.append(nums[i])
        subsets.append(path.copy())

        for j in range(i+1, len(nums)):
            self.subsetsOfPath(nums, j, path, subsets)

        path.pop()



    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for i in range(len(nums)):
            self.subsetsOfPath(nums, i, [], subsets)

        return subsets

"""
nums = [7]
subsets = [[]]

i = 0
    path =[7]
    subsets = [[], [7]]
"""
      

        