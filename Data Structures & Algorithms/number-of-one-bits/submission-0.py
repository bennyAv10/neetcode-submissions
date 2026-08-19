"""
Approache:
1. mask 1. iterating ans shifting right until number is 0. check the lowst bit each iteration. Time: O(logN)
2. n & (n-1) --> n-1 turns off the lowest 1s bit in n and turn on all lower bits. with the boolean n both are down - essentially you turn one bit off
time complexity is number of 1s bits in the number - not sure how to pexpress it in N but it's <= Log(N) (if all bits are on it's the same)

Correctnesss: see approach explanasion above

"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        """ Returns the number of 1 bits in the give number N
        """
        bit_count = 0
        while n:
            n= n & (n-1)
            bit_count+=1
        
        return bit_count

"""
test

6
110

bc=0
 n= 110 $ 101 = 100
 bc=1

 n = 100 & 011 = 0
 bc=2

 return 2

 adverserial cases:
 0, 
"""


        