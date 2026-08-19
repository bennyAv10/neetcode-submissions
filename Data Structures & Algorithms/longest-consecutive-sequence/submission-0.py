"""
Approaches:
1. sort the array (NlogN) and find the longest consecutive numbers - not O(N)
2.  heap - same runtime
3. hashmap to list. iterate over the list. if number below or above exist, unify below and above if not unified already. then add this element to the list
eventually scan throught the elements and find the longest one - Time: O(N) space O(N) (space makes sense as it's <=1k)

Invariant: before processing the ith number, we have the correct lists (united correctly) per number earlier in list
Preservation: if ith element is duplicated - nothing new. if it's a new number, then:
1. the previous and bove number don't exist yet - just create a new lst
2. eitehr of above or below create add the new number. if both exist if both exist connect both
not we have the correct cosecutive lists per number up to i
Consequence: base case is technily correctly has the variant (i=0) and with i=len(numss) the longest list is the asnwer
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return the longest consecutive list of numbers from the give list
        """
        seqs = {}

        for num in nums:
            if num in seqs:
                continue
            
            if num-1 in seqs or num+1 in seqs:
                if num-1 in seqs and num+1 in seqs:
                    seqs[num-1][0]+= seqs[num+1][0]
                    seqs[num+1] = seqs[num-1]
                    seqs[num] = seqs[num-1]
                elif num-1 in seqs:
                    seqs[num] = seqs[num-1]
                else: #num+1 in seqs
                    seqs[num] = seqs[num+1]
                seqs[num][0]+=1
            else:
                # val is a single cell list so we hold reference to same var across multiple keys
                seqs[num] = [1]

        max_seq=0
        for val in seqs.values():
            max_seq = max(val[0], max_seq)

        return max_seq

"""
[2,20,4,10,3,4,5]

s={}
2
2: [1]

20
2: [1]
20: [1]

4
2: [1]
4: [1]
20: [1]

10
2: [1]
4: [1]
20: [1]

3
2:[3]
3: ->2
4: ->2
20:[1]

5
2:[4]
2:->2
4:->2
5:-->2
3:

advereserial cases:
empty - return 0, connect two lists

butg 1: 
"""

        