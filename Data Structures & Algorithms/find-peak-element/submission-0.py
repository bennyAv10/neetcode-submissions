"""
Approach: binary search. compare mid with prev item if mid>mid-1 a peak is in [mid, ..., hi] (we started aincrease tredn which wither stop - that's the peak or not - hi is the peak)
else, mid-1->mid is decreasing trend which where starts is the peak or low is the peak --> [lo, mid)
Invariant: we know a peak exist at [lo, ..., hi] and we examining mid
Preservation: if mid > mid-1, either mid , .., hi keeps increasing (hi is a peak) ot stop increasing - there is the peak. same for low, ..., mid-1 for the other acse
Consequence: since the invariant is correct for the base case (lo=0, hi=last) and we cut by half each time, we'll eventually find it
Time: log(n)
Space: const
edge cases:
simngle lement - lo=hi=mid=0 --> we should return immidiately
lo=hi-1 --> mid=lo we'll keep getting in the same loop --> we should do ceiling


"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        lo=0
        hi=len(nums)-1

        while lo<hi:
            mid = math.ceil((lo+hi)/2)
            if nums[mid]<nums[mid-1]:
                hi = mid-1
            else:
                lo = mid


        return lo


"""
test:
1,2,3,1

lo=0, hi=3
mid=2
3>2 --> lo=2
mid = 3
1<3 hi-->2
lo=hi

--> 2
"""