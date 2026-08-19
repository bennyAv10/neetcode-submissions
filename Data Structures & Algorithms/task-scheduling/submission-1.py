"""
Approach: maintain a max heap by remaining occurences and a queue of blocked tasks (task, blocked until).
at any cpu cycle, push the alowed tasks now back to the heap, and pop the one with highest remainig tasks.
continue as long at queued or blocked isn't empty
Invariant: before scheduling the Ith cycle all scheduled ones are optimal and blocked_until is correct
Preservation: for the ith cycle getting the highest remaining occurence unblocked task and make it blocked for the next n cyclesis the most optimal step or sit idle
Consequence: invariant holds for the base acse, if we keep progressing eventually we have an optimal scheduling
time: O(max(klogk, n)) where k is number of tasks
Space: O(1) heap and queue size are of tasks type (A-Z) not individual tasks
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Returns the minimum number of CPU cycles for execute the given tasks assuming n CPU cycles are required between identical tasks
        """
        if n == 0:
            return len(tasks)
        tasks_queue = [(count, task) for task, count in collections.Counter(tasks).items()]
        heapq.heapify_max(tasks_queue)
        blocked_queue = collections.deque()
        cpu_cycle=0
        
        while tasks_queue or blocked_queue:
            while blocked_queue and blocked_queue[0][2] <= cpu_cycle:
                task, count, _ = blocked_queue.popleft()
                heapq.heappush_max(tasks_queue, (count,task))

            if tasks_queue:
                count, task = heapq.heappop_max(tasks_queue)
                if count>1:
                    blocked_queue.append((task, count-1, cpu_cycle+n+1))
            cpu_cycle +=1
        return cpu_cycle

"""
["X","X","Y","Y"], n = 2

q=(2:x, 2:y)
bq=[]
cc=0

q=(2:y)
bq=[x,1,3]
cc=1

q=()
bq=(x,1,3),(y,1,4)

cc=2
cc=3
bq=(y,1,4)
cc=4
bq=()
cc=5

advererial: n=0, 

bug 1: time limit exceeded. infinite loop? - the cpu_cyle+1 identation was wrong
bug 2: kept adding task with count-1 if count>0 but should have checked count>1
"""
            



        
        