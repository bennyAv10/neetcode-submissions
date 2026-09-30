"""
min number to remove to make all intervals non-overlapping is the same as maximizing non-overlapping internvals
approach: greediness - you take the one ending first as it's the least costly in terms of disqualifying other intervals. then you skip all overlapping ones (start[j]<end[i])
time: O(nlogn) for sorting with N= #intervals
space: you can sort in place. then just keep track on index O(1)
edge cases:
single interval
semi-overlapping in boundary isn't overlapping

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        min_overlapping = 0

        i=0
        while i < len(intervals):
            j=i+1
            while j < len(intervals) and intervals[j][0] < intervals[i][1]:
                min_overlapping+=1
                j+=1
            i=j
        
        return min_overlapping

"""
test:
= [[1,2],[2,4],[1,4]]

= [[1,2],[2,4],[1,4]]

i=0
 j=1
 i=1
 j=2
    min=1

bug1: typo

"""
        