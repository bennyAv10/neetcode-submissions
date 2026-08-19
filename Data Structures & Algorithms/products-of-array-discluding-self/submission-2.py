"""
edge cases:
empty

naive:
calculate products f all elements and divide by nums[i]
issue: can overflow - (but no overflow in Python) - no issue
time complexity 
all products = N
division fo recah cell N (indivudual numbers are small < 20 )
storage N for the response

the follow-up without using the division

2 lists
left - left[i] - products of num[0]...nums[i-1]

res[i] starts as right[i] = nums[i+1]*...*nums[last-i]

res[i] *= left[i]

time complexity 3N for 3 multiplication

we're implmenting the followup question which is slightly more time and storage expensive but more challanging
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        # [1, nums[0], nums[0]*nums[1], .., nums[0]*...*nums[last-1]]    
        left_products = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left_products[i] = left_products[i-1]*nums[i-1]
        
        # [nums[1]*...*nums[last], ..., 1]
        right_products = [1] *len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            right_products[i] = right_products[i+1]*nums[i+1]

        return [right_products[i]*left_products[i] for i in range(len(nums))]



        