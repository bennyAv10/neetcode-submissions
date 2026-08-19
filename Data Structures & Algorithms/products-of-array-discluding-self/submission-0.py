class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        no zeros - trivial
        one zero - same place is the rest
        two zeros
        """
        total = 1
        zero_count = 0
        zero_index = -1
        for i, n in enumerate(nums):
            if n == 0:
                zero_count +=1
                zero_index = i
            else:
                total *= n

            if zero_count == 2:
                break

            
        
        res = [0]*len(nums)
        if zero_count < 2:
            for i in range(len(res)):
                if zero_index == -1:
                    res[i] = total // nums[i]
                elif i == zero_index:
                    res[i] = total


        return res
        