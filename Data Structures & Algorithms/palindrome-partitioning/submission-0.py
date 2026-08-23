"""
(After using 3 hints)
Approach: backtracking with current paldroms, with i, and j adn at each position continue with both options. when you reach last index
you add it to results only if it's a playdrom
time 2^n * n - 2^n decision nodes where you either partition or not with each one you check if it's a palyndrom
space: O(N) excluding the output
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def bt(cur: list, i: int, j: int):
            if s[i:j+1] == s[i:j+1][::-1]:
                cur.append(s[i:j+1])
                if j == len(s)-1:
                    res.append(cur.copy())
                    cur.pop()
                    return

                bt(cur, j+1, j+1)
                cur.pop()
            if j!=len(s)-1:
                bt(cur, i, j+1)
        bt([], 0, 0)
        return res

"""
"aab"
res=[]

c=[], 0, 0
    c=["a"], 1, 1
        ["a", "a"], 2, 2
            ["a", "a", "b"]
        ["a"], 1,2

"""
        