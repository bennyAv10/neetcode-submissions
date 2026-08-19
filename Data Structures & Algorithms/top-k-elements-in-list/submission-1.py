"""
ege cases:
empty
all the same
all different \ two are the same - always unique

counter, then heap with counter as value and count as key in the size of k

then collect the k

time complexity - 
N - building the dictionary
klogk building heap

Storage: k 

Alternatives:
sort (quick\merge) - still need build the dictionary. sort it will be NLogN. stgrage is still k
bucket sort - time complexity n. storage n

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [num for _, num in heap]
        
        return res