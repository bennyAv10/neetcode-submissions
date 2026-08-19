"""
Approach: highest frequency task -1 *n(+1) +1 - you have a group of task and n idle ccles (which you can use for other tasks) or the total number of tasks
if there are multiple max frequency tasks you add one for each such case.
Design: counter dict. find max (linear). follow the formula

edge cases

Case 1

n=5
A=3

(3-1)*(5+1) +1 = 12
A.....A.....A

Case 2
n=1
A=3
B=2
C=2

ABCABC

case 3

n=3
A=2
B=2
AB..AB = 6

(2-1) * (3+1) + (count of highest frequency nuymbers) = 5

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_count = collections.Counter(tasks)
        max_freq = 0
        max_tasks = 0

        for freq in task_to_count.values():
            if freq > max_freq:
                max_freq = freq
                max_tasks = 1
            elif freq == max_freq:
                max_tasks+=1

        return max(len(tasks), (max_freq-1)*(n+1) + max_tasks)

"""
tests

XXYY, n=2
x: 2
y:2

max=2
tasks=2

(2-1)*(2+1) +2 =5

AAABC, n=3

A: 3
B: 1
C:1

max=3
tasks=1

(3-1)*(3+1)+1 = 9

bug 1: AAB, n=0 - root casue with n=0 (and also other n) the idle slots between most frequent tasks are not enough. fix: added max with len of tasks
"""
       