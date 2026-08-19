"""
**UPDATE**: my understanding below was wrong, I should have always iterate for 32 times
Approach: mask the lowest bit and set it to the result lowest bit. with each iteration you shift right the input and shift left the output.
you stop with input is 0. Time: O(logN)
Direct proof: at each iteration you take the current lowest from the input ans set it to the next bit in the result everytime you shift the result left.
i.e. the first bit originally from the input lowest bit eventually becomes ther esults highest bit
Adereserial: 
0 --> 0
negative is excluded

"""
class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            output = output << 1
            output |= n&1

            n = n >> 1

        return output

"""
n=100

o=0

o=0
n=10

o=0
n=1

0=1
n=0

bug 1: i didn't keep pushing all the way 32 bit. it's understanding bug (See the update above)
total time: 

"""
        