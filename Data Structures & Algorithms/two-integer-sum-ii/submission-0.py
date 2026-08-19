"""
naive approach:
N^2 - for each element lok at all others if they sumup to target
this don't leverage the sorted assumption

with sorted 
if i0 and j0 > target - we can siqualify i0 and any j>j0, and also any i>i0 with any j>=j0 - The only possible candidates
i<i0 with any J or j<j0 with any i 

if i0 and j0 < target - the only possible candidates i>i0 with any J or J>j0 with any I

Approach: two pointers starting at first and last elements. if i0+j0 < target we move i0 forward. if io+j0>target we move last backward
Invariant: assuming we know i and j can only come from [I,..., J] (Which is true when we start with first and last)
and I+J < target - the new possible domain is [i+1, ..., j]
similariliy if i+j> target the only domain is [i, ..., j-1]

Time complexity: N - at each iteration we move wither left or right
Space: const - two pointers

testing with example:
[1,2,3,4], 3
l=0
r=3
1+4=5>3
l=0
r=2
1+3=4>3
l=0
r=1
1+2=3 exactly target return l+1, r+1

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a non-decreasing sorted array
        Return 1-based index of two indices where their sum equals target
        The implementation assumes exectly single solution exists
        """
        l=0
        r=len(numbers)-1

        while l<r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l+1, r+1] # 1-based index
            elif current_sum < target:
                l += 1
            else: # current_sum > target
                r -= 1

        raise ValueError("Couldn't find a solution")
