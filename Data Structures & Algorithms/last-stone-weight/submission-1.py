"""
Approach: heapify the list. take the two heaviests and either both smashed ot you get a single smalleer stoner. push it to the heap back.
you stop when the heap is empty. then you left with either zero or a single stone
Time: heapify is O(N) then each push pop is log(n) --> total Nlog(N)
Alternative: sorting. same cost (quick sort avg. mergesort both)
Invariant: before pulling the Ith stone we already have the survived stone so far correctly the results of smashing the 0, ..., i-1 heaviest stones
Preservation: since it's a heap the next stone is the heaviest among the rest --> is the Ith heaviest. following the protocol preserve the invariant for 0, ..., Ith
Consequence: base case tih I=0 thei nvariant holds --> when i=last we dne
Space: O(1). the heap is using the given list
Edge cases:
empty - excluded
one
two stones same weight
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        assuming smashing two heaviest stones at a time
        """
        heapq.heapify_max(stones)

        while len(stones) >= 2:            
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            
            first -= second
            if first != 0:
                heapq.heappush_max(stones, first)

        return stones[0] if stones else 0

"""
test:

[2,3,6,2,4] --> [6, 4, 3, 2, 2]

6,4 --> 2

[3, 2, 2, 2]

3, 2 -> 1
[2, 2, 1]

2, 2 -> 0
[1]

--> 1

edge cases: size 1
conditions to check:
    first bigger, first equal, first equal with no extra stones
    left with one and left with zero


stones=[7,6,7,6,9]

[9,7,7,6,6]

9,7->2
[7,6,6,2]

7,6 ->1
[6,2,1]
6,2 -> 4
[4,1]
4,1 ->3
3
"""
        