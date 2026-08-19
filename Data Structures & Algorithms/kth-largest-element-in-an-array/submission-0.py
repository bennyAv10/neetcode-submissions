"""
Alternatives:

sorting decreased order and return the kth elment - O(NlogN). can sort in place or spcae N
heap - min heap of size k. keep pushpop (keep the k biggest) - Nlogk. spcae k 
quick select - variant of quikc sort just recursing into one half every time. O(N) avg - n +n/2 + n/4 ~= 2N. worst case N^2 (if pivot lands in the boundary, so every lavel just reduced by one)

Approach: heap. good enough for not extream N and to practice heap. with very large N will consider do quick select + randomized pivot + timer interruption and retry

Invariant: when processing index i>k, the min-heap contains the largest k elements fro nums[:i]
Preservation: doing pushpop with nums[i] keeps the k largest from nums[:i+1]
Consequence: with i=len(nums). the heap contains the klarest from all nums, with the kth element is first (min heap)
Time: O(Nlogk) - N pushpop to a k size heap
Space:k
Edge cases
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Returns the K largest element in the array
        """
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])

        return heap[0]


"""
Test:
nums = [2,3,1,5,4], k = 2

h = [2,3]

1
h = [2,3]
5
h = [3,5]
4
h=[4,5]

--> 4

"""

        