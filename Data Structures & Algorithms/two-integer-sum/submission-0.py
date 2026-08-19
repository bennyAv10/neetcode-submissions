class Solution:
    """
    using dict with T=N and S=N
    alternative: Sort and go with two pointers
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing_nums = {}
        for i in range(len(nums)):
            missing_nums[target-nums[i]] = i 
        
        for i in range(len(nums)):            
            if nums[i] in missing_nums:
                other_index = missing_nums[nums[i]]
                if other_index  != i:
                    return [i, other_index] if i < other_index else [other_index, i]
        
        return [0,0]