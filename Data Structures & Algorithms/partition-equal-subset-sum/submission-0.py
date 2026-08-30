"""
two equally sum subsets exist IIF (1) the total sum is even and (2) there is a subset whose sum = total/2
property (1) is easy. property (2) is the subset with target sum problem the state we're tracking is (remaining amount, prefix)
going over each number and answering the question, can i get to this target assuming dp[a-num] (dp[a-num] comes from previus nums)
time: O(sum/2)*O(nums)
since nums<=100 and nums[i]<=50 --> 50*100 = 50,000 -> 5*10^4 --> time coplexity 5*10^4*5*10^1 ~=2.5 *10^6
space: O(sum/2)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total//2
        if target != total/2:
            # odd number
            return False
        
        dp = [False]*(target+1)
        dp[0] = True # you can get to 0 by empty subset
        for num in nums:
            for a in range(target, num-1, -1):
                if dp[a-num]: dp[a]=True #you can get total of a-num without num --> you can get total of a with num
        
        return dp[-1]

"""
[1,2,3,4]

sum = 10
sum//2 = 5

dp=[T, F, F, F, F]

1
    5
    4
    3
    2
    1
        dp[1]=T

2
    5
    4
    3
        dp[3]=T
    2
        d[2]=T
3
    5
    4
    3
4

"""