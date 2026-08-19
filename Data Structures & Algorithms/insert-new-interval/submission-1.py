"""
Approach: iterate while interval[i][start] is smaller than new interval start. now you insert the new interval.
now you need deduplicate: start with the new intervaland stop when max_end < start
Invariant/preservation: 
first iteration finding th einsertion point:
invariant:before processing Ith element we have inervals 0...(i-1) with each one start(k)<=end(k)<start(k+1) and the new interval with start > any start(0...i-1)
preservation: with ith element eitehr start(i) is also < the start of new with that we preserve the invariant or we found the insertion point
consequence: invariant is true about baseline and we preserve it --> we found an insertion point where we have i with start point>= new interval start point
ans some j>i with start(j) > new interval end or new interval end goes all the way to the end
dedup iteration:
invariant: before processign j we know that for i, ..., j-1 interval[k]pstart]>=new_interval[start] but interval[k][start] <= new_interval[end] --> new interval is ioverlap with any k.
preservation: if interval[j][start] > new[end] we foudn the end of the overlapping
consequence: base case holds
time: inserting in the middle and delting is O(n)
space: const we reuse the same list
edge cases:
new interval at the beginng - no overlap
new interval at the end - no overlap
new interval in teh middle with oval all the way to the end
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        
        i = 0
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            i+=1
        start=newInterval[0]
        if i<len(intervals):
            start=min(newInterval[0], intervals[i][0])
        intervals.insert(i,[start, newInterval[1]])
        
        j=i+1
        max_end = newInterval[1]
        while j<len(intervals) and intervals[j][0] <= newInterval[1]:
            max_end = max(max_end, intervals[j][1])
            j+=1

        intervals[i][1] = max_end 
        del intervals[i+1:j]

        return intervals
"""
intervals = [[1,3],[4,6]], newInterval = [2,5]

i=0
3>=2 --> insertion

intervals = [[1,5],[4,6]]

j=1
    4<5
    max_end=6
j=2 >=len

del 0:2

re trurn [[1,6]]


boundary:
empty intervals, no overlap new at the beginng, no overlap in the middle
failure scan: 
adversarial:


"""