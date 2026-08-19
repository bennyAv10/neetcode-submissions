"""
Approach 1: backtracking/DP with each i where nums[i]=n, you try k=[n...1]. use recursion (python allow up to 1k which is the limit here).
if i = last return true. if i in failed set retrun false. otherwise, keep trying from k=n...1
Time=O(N)
Space=O(N) for the stack

Approach 2: start from the end. use a boolean list initalized to false. set to true if can reach to true within allowed distance (keep track of last_reacing).
Time: O(N)
Space: O(N)
better than first approach as no stack depth limit

Approach 3: just keep track on last reaching (initialized to last) from the end. then coming return of last reaching is 0 index. time: N space 1
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reaching = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_reaching:
                last_reaching = i

        return last_reaching==0

"""
[1,2,0,1,0]

lr=4

i=3
lr=3

i=2

i=1
lr=1

i=0
lr=0 --> true

[1,2,1,0,1]

lr=4

i=3

i=2

i=1
i=0

False
"""

        