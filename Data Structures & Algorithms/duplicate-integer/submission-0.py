class Solution:
    """
    1. sorting - O(nlogn), 1
    2. hash O(n), O(n)

    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        