"""
originally: [>>>]
after rotation: [>>><>>] [x0, x1, ..., min, y0, ..., yn]


Approach: binary search - You can by half in each iteration and fine the half containing the min
Invariant: Assuming a rotated sorted range with min somewhere - [x0, x1, ..., min, y0, ..., yn] any y is smaller or equal to any x
if l > mid --> rotation is in left side
elif  mid > r --> is in the right
else:
    no rotation l is min
Time complexity: Log(N)

edge cases:
all elements are the same -- any answer is right
empty (assuming len >=1)

test:

[3,4,5,6,1,2]

l=0, r=5
mid = 2

3<5 but 5 > 2
l=3, r=5
mid = 4

6>1
l=4, r=5
mid=4
return 1

example 2
[4,5,0,1,2,3]

l = 0, r =5
mid = 2

4>0
l=0, r=2
mid = 1
4<5 but 5>0
l=2

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r)//2

            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid +1
            else:
                return nums[l]

        return nums[l]


        