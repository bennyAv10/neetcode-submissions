class Solution:
    """
    1. start with hash table O(N) time, O(2000) space
    2. creaet a list of pairs - O(N), o(2k)
    3. sort the list O(2klog(2k))
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        freq_val = [(v, k) for k, v in counter.items()]
        freq_val.sort(reverse=True)
        return [b for (a,b) in freq_val[:k]]

