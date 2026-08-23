"""
Brute Force: for echa i and j>i check the product of nums[i]..., nums[j]. Time: O(N^3) for each i, j, (N^2 options) you multiple O(N) elements. space: O(1)
backtracking (Is it backtracking or different method?): you start with each i, and do bt. for each j yu call with the running product i-j-1 and multiply by j and check if it's bigger than max. Time: O(N^2) you start with each index and multiply along the rest of the list
dynamic programing: starting with all products of len 1 (which is the lements themselves). then with each iteration go one length up.
time: O(N^2) - each length has O(N) products and you have O(N) lengths
edge cases:
    single element is the max
    0
cadane variant: run over the list. keep track of max (initialized to nums[0]) and min_negative (initialized to 0).
current - current product restart for 0 or negative
current_negative - the min current negative reset with another negative (--> current) or with 0
current is zero - break everything

when encoutnering 0 check if current>max
when encountering potivie multiply both current and current_negative
when encoutnering negative, if negative < 0 --> current = negative*nums[i] and negative--> 0. otherwise, 
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for num in nums[1:]:
            prev_max = cur_max
            cur_max = max(num, prev_max*num, cur_min*num)
            cur_min=min(num, cur_min*num, prev_max*num)
            best = max(best, cur_max)
            

        return best

"""
 [2,4,-3,5]

m=2
c=1
n=0

0
    c=2
    n=0
1
    c=8
    n=0
2
    m=8
    c=1
    n=-24
3
    c=3
    n=-120

    bug 1: all negatives with 0 separating them 0 should be the max but I initilized current to 1
"""   