"""
Approach: 
1. sort in decreasing order
2. start backtracking from each number
3, keep adding start from the same index and later
4. any succussful is added
5. unsuccessful --> > target return

Invariant: the running sum  contain the bigger elements
Preservation: we complete current or smaller element

Time: 
Sapce:
"""
class Solution:
    def completeCombinationSum(self, nums: list[list[int]], target: int, current_index: int, current_sum: int, current_elements: list[int]) -> list[list[int]]:
        new_sum = current_sum + nums[current_index]
        new_elements = current_elements+[nums[current_index]]
        if  new_sum > target:
            return []
        
        if new_sum == target:
            return [new_elements]
        
        res = []
        for i in range(current_index, len(nums)):
            res += self.completeCombinationSum(nums, target, current_index=i, current_sum=new_sum, current_elements=new_elements)
        
        return res
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)
        result = []
        for i in range(len(nums)):
            result += self.completeCombinationSum(nums, target, current_index=i, current_sum=0, current_elements=[])

        return result

"""
test - example 1 [2,5,6,9]. target = 9

sort - [9,6,5,2]


9
 --> [9] -- candidate

6
    6
    new sum 12
    5
    new_sum 11 --> []

    2  --> 8 --> []

5
    5 --> 10
    2
        2 --> 9!

2
    2
        2
            2

running:
 issues 1 - sort argument decrease instead of reverese
 issue 2 - new elements spelling
 issue 3 - result spelling
"""
        