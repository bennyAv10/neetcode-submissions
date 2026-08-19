"""
Approach: sort intervals by start. iterate - if next start is smaller or equal to current end merge them with current start and max end
Invariant: before processing interval i+1 we know, first i intervals are not overlapping.
Preservation: with i+1, if start[i+1] > end[i] --> i+1 isn't overlapping -->otherwise, we merge it with with i and now all the original i+1 intervals are representd as non-overlapping ones
Time: O(nlog(n)) for sorting + O(n) for merging
Space: O(N)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Returns the given intervals with overlapping ones merged
        """
        res = []
        prev_end=-1
        intervals.sort()
        for start,end in intervals:
            if start <= prev_end:
                res[-1][1] = max(end, prev_end)
            else:
                res.append([start, end])

            prev_end = res[-1][1]

        return res

"""
[[1,3],[1,5],[6,7]]

sort stays the same

res []
prev = -1

1,3

start>-1

res = [1,3]
pe=3

1,5
1<pe-3
res=[1,5]
pe=5

6,7
6>5
res=[[1,5],[6,7]]



"""



        