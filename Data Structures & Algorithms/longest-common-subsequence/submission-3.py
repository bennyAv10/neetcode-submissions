"""
Approach: init 2d board of len(text1)*len(text2). start with last row (=last letter in text1 with any letter of text2).
last column is last character in text2 with any letter of text1.
now any other cell is longest of cell beloo or cell to the right + 1 if text1[i]=text2[j]. the board should tell you if text1[i] and text2[j] were used
Invariant: before processing i,j, we know that for every x>i and for x=i and y>j x,y correctly state the longest commen subsequence for text1[x:] and text2[y:] and 
if x,y letter was used or not for that longest subsequence
preservation: looking at text1[i:] and text2[j:] the longest subsequence  is the longest to the right or to the left with the current if it matched and wasn't used
Consequence: the invariant is correct for the last row and the last column, so it's correct for x,y =0,0 which answers the longest subsequence for text1 and text2
Time:
Space:
edge case:
letter repeating twce in one string but not the other - don't double count
optimizatioon - we only need one row - we keep overriding the previous col and rows
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_so_far = [[0, False, False]] * len(text2)
        # print(max_so_far, text2)

        if text1[-1] == text2[-1]:
            max_so_far[-1] = [1, True, True]
        for j in range(len(text2)-2, -1, -1):
            # print(j, len(max_so_far))
            if max_so_far[j+1][0] == 1:
                max_so_far[j] = [1, True, False]
            elif text1[-1] == text2[j]:
                max_so_far[j] = [1, True, True]

        for i in range(len(text1)-2, -1, -1):
            
            if max_so_far[-1][0] == 1:
                max_so_far[-1][1] = False # we don't need text1[i] for the subsequence
            elif text1[i] == text2[-1]:
                max_so_far[-1] = [1, True, True]

            for j in range(len(text2)-2, -1, -1):
                # print(i,j, max_so_far)
                option1 = max_so_far[j+1][0] +(1 if text1[i] == text2[j] and max_so_far[j+1][1]== False else 0)
                option2 = max_so_far[j][0] +(1 if text1[i] == text2[j] and max_so_far[j][2]== False else 0)

                if option1 >= option2:
                    max_so_far[j]=[option1, max_so_far[j+1][1], False]
                    if text1[i] == text2[j] and max_so_far[j+1][1]== False:
                        max_so_far[j][1] = True
                        max_so_far[j][2] = True

                else:
                    max_so_far[j][0] = option2
                    max_so_far[j][1] = False
                    if text1[i] == text2[j] and max_so_far[j][2]== False:
                        max_so_far[j][1] = True
                        max_so_far[j][2] = True
                
                # if text1[i]==text2[j]:
                #     max_so_far[j][1] = True
                #     max_so_far[j][2] = True
            # print(i, max_so_far)

        return max_so_far[0][0]

"""
testing:

Input: text1 = "cat", text2 = "crabt" 

 i = 2
    j = 4
        1,t,t
    j = 3
        1,t,f
    j = 2
        1,t,f
    j=1
        1,t,f
    j=0
        1,t,f
i=1 -->a
    j = 4 -->t
        1,f,t
    j = 3 -->b
        1,f,t
    j = 2 --> a
        2,t,t
    j=1 --> -->r
        2, t, f
    j=0 -> c
        2,t,f
i=0 -> c
    j = 4 t
        1,f,t
    j = 3 b
        1,f,t
    j = 2 a
        2,f,t
    j=1 - r
        2,f,t
    j=0 c
        3,t,t

"""






        