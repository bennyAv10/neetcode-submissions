"""
naive algortihm: recursion. you count add way on one step + two steps. you stop when reching the end or only one step left and return one
time: T(N)=T(N)+T(N+1) - time doubled for linear growth --> O(2^N)

This is actually fibonacci

DP Approach: caching result. iteratively to save on stack
Invariant: one way to climb one step. two ways to climb two steps. higher N you can climg one step and have F(N-1) or climb two and have F(N-2)
Time Complexity: O(N) you inly "visit" each i once
Space Complexity: O(N) - cache
Edge cases: 
n = 0 excluded
n = 1 (stop)
 n = 2 (stop)

integer overflow --> n <=45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [0]*n
        cache[0] = 1 # 1 step
        
        if n>1:
            cache[1] = 2 # 2 steps

        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n-1]

        