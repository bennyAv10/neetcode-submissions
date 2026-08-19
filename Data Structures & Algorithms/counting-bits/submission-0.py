"""
Approaches:
1. iterate over numbers and count number of bits - Time: NLogN (LogN to count 1's bits in a single number)
2. (Only after reading hints hints). with every power of 2 you start with 1 digit (E.g. 1, 10, or 100) and the other digits follow exectly the numbers from 0 until that number.
that enable a dp approach - with every power of 2 you starts with dp - the way you check if a number is power of 2 is n&n-1 = 1 - Time: O(N). Space: O(N)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] *(n+1)
        for i in range(1, n+1):
            if i&(i-1) == 0: # i ispower of 2
                dp[i] = 1  # power of 2 number has a single 1
                base = 1
            else:
                dp[i] = dp[base]+1
                base += 1
        return dp

"""
Input: n = 4

dp =[0,0,0,0,0]


i=1
dp =[0,1,0,0,0]
base=1
i=2
dp =[0,1,1,0,0]
base=1
i=3
dp =[0,1,1,2,0]
i=4
dp =[0,1,1,2,1]

Adverserial:
n=0 - not entering the loop


i=15 

last power of 2 of 8 --> 9-->dp[1]+1 1001 15:1111 -> dp(7)+1
"""

        