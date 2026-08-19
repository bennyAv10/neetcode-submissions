"""
if sum of cost<= sum of gas it can be done
Start from begining. runnging sum of gas - cost. once getting negative starting location is next place. if prev ones failed, last one is the start

Getting to negative running sum diff disqualifies all previous places and not only the first place
since the total sum diff is non-negative, if all other places disqualified, the last place is the only candidate
Time: O(N) sum, + one iteration
Space: O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        balance = 0
        start=0

        for i in range(len(gas)-1):
            balance += (gas[i]-cost[i])

            if balance<0:
                balance=0
                start=i+1
        
        return start

"""
Input: gas = [1,2,3], cost = [2,3,2]

sum(gas)-sum(cost) = 6 cost =7 
-1

Input: gas = [1,2,3,4], cost = [2,2,4,1]

sum(gas)-sum(cost)=10-9=1

b=0
s=0

0
b=-1
b=0
s=1

1
b=0

2
b=-1

b=0
s=3


"""
        