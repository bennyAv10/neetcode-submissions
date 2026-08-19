class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        left_product and right product
        left_product[i] = nums[0]*...*nums[i-1]
        right product is smilar but to the right

        now res[i] = left[i]*right[i]
        """
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_product[i]= right_product[i+1]*nums[i+1]
        
        for i in range(len(left_product)):
            left_product[i] *= right_product[i]
        
        return left_product

    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
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
        