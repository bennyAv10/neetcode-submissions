"""
naive approach for each i find the highest j - time N^2

better:
keep track on min(init -1), and max_profit (init 0)

Approach: keep track on min element so far, in any new element that's not a new min, check if potential profit is bigger
Invariant: we come to j with min_index=i and max_profit=X. nums[j] is either smaller than nums[i] so it should be the min for future selling
or it's bigger than last selling point - meaning it's better to sell now
Time complexity: O(N) - 
Space: O(1)
edge cases:
empty (excluded)
price keep going up - just don't buy and get profit 0 - don't lose

emulating with example 1

min_price=10
max_profit = 0

10 -10 not bigger
1 < 10 (min)
min_proce = 1

5 > min_price but 5-1>0
max_profit=4
6>min_price but 6-1>4
max_profit =5 




"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > max_profit:
                max_profit=price-min_price

        return max_profit
