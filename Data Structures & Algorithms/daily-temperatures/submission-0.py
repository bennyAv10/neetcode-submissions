"""
how many day from i to warmer day

naive solution O(N^2)

for each day scan the temps array and find a warmer day

(Had to use all the hints - 4)

iterate from left to right
when trend is teh same or lower, no update is needed
when it goes up you need to update all recent days until nn-colder

which means for any i the colder days, are at the top of the stack.

mean we can pop them. and once we stop poping, the rest are equal or warmer
time O(N) - we look at i twice at most
space O(N) stack when all days are just codler.

try 1 - wrong answer
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Returns the number of dyas until a warmer day for each day in `tempratures`

        Time Complexity O(N) for N- number of days
        """

        stack = collections.deque()
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cooler_day_index = stack.pop()
                res[cooler_day_index] = i-cooler_day_index

            stack.append(i)

        return res



        