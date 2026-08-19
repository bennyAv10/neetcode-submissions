"""
Approach: for any i, j LCS(i, j) is: if text1[i]!=text2[j] the max of LCS(i, j+1) and LCS(j+1).
if text1[i]=text2[j] then it's LCS(i+1, j+1)+1. if i or j ar the last then it's either previous is 1 or current is a match
Invariant: before processing the suffixes text1[i:] and text2[j:] we already know LCS(>=i, >j) and LCS(>i, >=j)
Preservation: if text1[i] != text2[j] then LCS(i,j) is max LCS(i+1, j) and LCS(i, j+1) if they're equal LCS(i,j)=LCS(i+1,j+1)+1.
next when we process either LCS(i, j-1) or LCS(i-1, last) the invariant holds
Consequence: for the base case of lsat, last it's eitehr 1 if match or 0
Time: O(N*K) for N=len(text1) and K=len(text2)
space: O(N) *O(K) - we could optimize for last two rows only, but I rathered focus on correctness
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0] * len(text2) for i in range(len(text1))]
        lcs[-1][-1] = 1 if text1[-1] == text2[-1] else 0
        for j in range(len(text2)-2, -1, -1):
            if lcs[-1][j+1] ==1 or text1[-1] == text2[j]:
                lcs[-1][j] = 1
        for i in range(len(text1)-2, -1, -1):
            lcs[i][-1] = 1 if text1[i] == text2[-1] else lcs[i+1][-1]
            
            for j in range(len(text2)-2, -1, -1):
                if text1[i] == text2[j]:
                    lcs[i][j] = lcs[i+1][j+1]+1
                else:
                    lcs[i][j] = max(lcs[i][j+1], lcs[i+1][j])

        return lcs[0][0]

"""
text1 = "cat", text2 = "crabt" 

lcs =
0,0,0,0,0
0,0,0,0,0
0,0,0,0,0

0,0,0,0,0
0,0,0,0,0
1,1,1,1,1

i=1
3,2,2,1,1
2,2,2,1,1
1,1,1,1,1

Advererial: too tired for this


bug
text1="abcba"
text2="abcbcba"

bug was 2d array declared with [[0]*len]*len
"""


                
        






        