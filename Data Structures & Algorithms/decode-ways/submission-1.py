"""
0 can only be a single digit of 10 or 20. 
1,2 could be single digit number, tens digit (2 only if the single is <=6), or sinlge digit of two digits number (only if digit to the left is 1 or 2).
3-9 can either be a single digit of two digits number or of a single digit number
Approach: processing from right to left. when processing the i'th digit. we count how many diffrent ways we interpret
1. if i+1 = 0 - the only interpretation to i is single digit oof two digits number dp[i] = dp[i+2] (we assume input is valid. otherwise, we'll need validate)
2. if i=0 just assign dp[i]=dp[i+1], but we won't really use it
2. if i=1 or i=2 and i+1<=6 - dp[i] = dp[i+1] (i is a new single number) + dp[i+2] (i is the 10s digit of i+1)
3. if it's 3-9 or 2 with i+1>6 - dp[i] = dp[i+1] (i is new number)

Invariant: before processing Ith element we know the number of way for k>i
Preservation: With the described approach and assuming legal input, we now know the number of ways for the Ith element
Consequence: base case is dp[i+1]=1 for the last element and 0 for i+2
Time: O(N)
Space: O(1) we only need two last places

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Number of ways to decode element which originally encoded from uppercae A-Z --> 1-26
        """
        prev=1
        current=1
        current_digit = int(s[-1])

        for i in range(len(s)-2, -1, -1):
            prev_digit = current_digit
            current_digit = int(s[i])
            
            if prev_digit == 0:
                if current_digit == 0 or current_digit>2:
                    return 0 # invalid
                else:
                    next_count = prev
            elif current_digit == 0:
                next_count = 0
            elif prev_digit != 0 and (current_digit == 1 or (current_digit == 2 and prev_digit<=6)):
                next_count = current+prev
            else: # i= 3-9 or (2 with next>6)
                next_count=current
            prev=current
            current=next_count
            print(i, current)
        
        if current_digit == 0:
            return 0
        else:
            return current

"""
2101

p=1
c=1
cd=1

i=2
    pd=1
    cd=0
    nc=1
    p=1
    c=1
i=1
    pd=0
    cd=1

i=2
test

12

p=1
c=1

1
next= 1+1

01
p=1
c=1

0
next=1

bug 1: always return 1 - issue decded isn't number but string
bug 2: invalid case is actually happens and explicitly stated in teh examples
bug 3: 2101 return 2 instead of 3



"""


            
        