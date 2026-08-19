"""
once a letter is in a substring you must go until last occurence of this letter
Approach: first counter. iterating over once adding decrease frm counter and if not 0 add to a set. remove from set once it's 0. when 0 move to next
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = collections.Counter(s)
        res = []

        current = set()
        prev_index = -1

        for i in range(len(s)):
            c = s[i]

            counter[c]-=1

            if counter[c]>0 and c not in current:
                current.add(c)
            elif counter[c]==0 and c in current:
                current.remove(c)

            if not current:
                res.append(i-prev_index)
                prev_index=i

        return res

"""
Input: s = "xyxxyzbzbbisl"

c=x:3, y:2,z:2,b:3,i:1,s:1,l:1
r=[]
cu={}
pi=-1

i=0,x
x:2
cu={x}

i=1,y
y:1
cu={x,y}

i=2,x
x:1

i=3,x
x:0
cu={y}

i=4,y
y:0
cu={}
res=[5,]
pi=4

i=5,z
z:1
cu={z}

i=6,b
b:2
cu={z,b}

i=7,z
z:0
cu={b}

i=8,b
b:1

i=9,b
cu={}
res=[5,5]
pi=9



"""

        




        