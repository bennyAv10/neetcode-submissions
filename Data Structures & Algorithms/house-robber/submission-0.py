"""
Approach: in the Ith house I can either take max(i-1) and skip i or max(i-2)+i. we carry both maxes
Invariant: assumin we know max_ending_at_prev and max_ending_at_prev_prev, max_ending_at_current is
either taking max_ending_at_prev and skip current or max_ending_at_prev_prev+current. 
after the very last item, the max of the two is the max
Time: linear
Space: constant
exampl test:
[1,1,3,3]
mp = 0
mpp = 0

i=0
mc = max(0+1, 0) = 1

mp = 1
mpp = 0

i=1
mc = max(0+1, 1) 

mp = 1
mpp = 1

i=2
mc = max(1+3, 1) 

mp=3
mpp=1

i=3
mc = max(1+3, 3)

mp=4
mpp=3

return 4

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        """ House robbing optimizer

        Optimization assumes two adjucent houses can't be robbed

        Args:
            nums: "Available" money in each house

        Returns:
            max amount of money
        """
        max_ending_at_prev = 0
        max_ending_at_prev_prev = 0

        for num in nums:
            max_ending_at_current = max(max_ending_at_prev, max_ending_at_prev_prev + num)

            max_ending_at_prev, max_ending_at_prev_prev = max_ending_at_current, max_ending_at_prev

        return max_ending_at_prev

"""
testing:
[2,9,8,3,6]


mp = 0
mpp = 0

i=0
mp = 2
mpp = 0

i=1
mp=9
mpp=2

i=2
mp=10
mpp=9

i=3
mp=11
mpp=10

i=4
mp=16
mpp=11
"""

        