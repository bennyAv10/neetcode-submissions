"""
non negative numbers
up to 20

Approach: keep a hasmap keyed by all possible sums for the current element and value is number of ways. for each new element calculate possible targets

teh state per i: how many possible sums for [0:i+1] assuming we can either add or substract each item
initialize to (nums[0]: 1, -nums[0]: 1)
for each i 1:end

    i.e. for k,v in map
        next_map[map[k]+nums[i]] +=v
        next_map[map[k]-nums[i] +=v
    map=next_map

eventually return map target

time: at each i number of sums < 2^i - i.e. 2+4+...n^2 = ~= 2^n 2^20 = (2^10)^2 ~=1m
space O(2^n)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_to_count = collections.defaultdict(int)
        sum_to_count[nums[0]]=1
        sum_to_count[-1*nums[0]]+=1

        for i in range(1,len(nums)):
            next_sum_to_count = collections.defaultdict(int)
            for sum, count in sum_to_count.items():
                next_sum_to_count[sum+nums[i]]+= count
                next_sum_to_count[sum-nums[i]]+=count
            sum_to_count=next_sum_to_count
        
        return sum_to_count[target]


"""
2,2,2

stc={2:1, -2:1}

2
    stc={0:2, 4:1, -4:1} 0 -> (2,-1), 

2
    stc={2:3, -2:3, 6:1, -6:1}

bug 1 [0,0,0,0,0,0,0,0,1]
target=1

128 instead of 256
"""

        