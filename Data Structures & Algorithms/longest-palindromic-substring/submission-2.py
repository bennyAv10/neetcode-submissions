"""
insights:
1. e asingle letter is a palindrom
2. if s[i:j] is a plaindrom and s[i-1] == s[j] - then s[i-1:j+1] is a palindrom

Approaches:
1. we already know for each i s[i:i+1] is a plaindrom. we can also start with palyndroms of size 0.use dp and keep tracking on all palindroms of a given length. extending them each time by 2.
keep track of the longest one. Time: N initial palindroms which in worst case you keep extenting each one by 2 so N*N/2 == O(N^2). Space: O(N)
2. brute force - for any i yu try with any j -- for a given i, and j it's N, so for a give i it's N^2, so for all of them it's N^3 - worse

let's go with #1 - 
Invariant: before findding palyndroms of size l, we already know all the palndroms of size l-1
Preservation: for any given palyndrom of size l-1 at s[i:j] there is a palyndrom of size l+1 IIF s[i-1] == s[j] --> we know found palyndroms of the next size
Consequence: since a single letter is a palyndrom, and a 0 is a palyndrom we have the base case, and continue increasing we have palyndroms of even and odd length
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palyndroms = [(i,i+1) for i in range(len(s))] + [(i, i) for i in range(len(s))]
        next_palyndroms = palyndroms
        n=0
        while next_palyndroms:
            palyndroms = next_palyndroms
            next_palyndroms = []            
            for i, j in palyndroms:
                if i>0 and j<len(s) and s[i-1] == s[j]:
                    next_palyndroms.append((i-1,j+1))
            n+=1
            

        i,j= palyndroms[0]
        return s[i:j]

"""
Input: s = "ababd"

p=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,0),(1,1),(2,2),(3,3),(4,4)]

np=p

0,1
1,2
--> 0,3
2,3 --> 1,4
3,4 
4,5
0,0
1,1
2,2
3,3
4,4

np=0,3 - 1,4

0,3
1,4
np is empty
retrn p[0]

bug 1: infinit loop. spelling error in palyndrom assignment
bug 2: returned indices instead of the palyndrom itself
"""


        