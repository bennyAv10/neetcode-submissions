"""
Approach: 
Step #1 - create a copy of the list which also includes the original index. sort it by enqueue time.
Step 2# - create a priority queue (min heap) according to processign time. the clock starts at the first task time. at each time 
you enqueue all current tasks (tasks with enqueue time <= now), pop the min task, add it to ther esult and progress the time by this task processing time

first pull all current tasksto the priority queue (bu length) with index (processing time, index)
next, pop hte firt one from the queue (min heap), add the index to ther response and set the timer forward by processign time 
time: O(nLogN) - sorting is nLogN and also the heap across all tasks
Space - N for the sroted list, result and the heap
Invariant: before processing tasks enqueued at time k, we already know for tasks enqued earlier they're either already processed by time k or still in the queue
Preservation: adding to the min heap all tasks enqueued at time k to the earlier unproccessde tasks. now, the task with smaller processing time is processed
Consequence: base case holds the variant --> the result order is correct
"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        returns the processing order of list of tasks with each task [enqueTime, procissing Duration]
        The protocol is that the shortest available task is executed at any given time
        """

        tasks_with_index = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        tasks_with_index.sort()

        queue = []
        i = 0
        result = []
        current_time=0
        while queue or i<len(tasks_with_index):
            if not queue:
                current_time = max(current_time, tasks_with_index[i][0])
            while i<len(tasks_with_index) and tasks_with_index[i][0] <= current_time:
                heapq.heappush(queue, (tasks_with_index[i][1], tasks_with_index[i][2]))
                i+=1
            
            
            processing_time, index = heapq.heappop(queue)
            result.append(index)
            current_time+=processing_time
            

        return result
"""
tasks = [[1,4],[3,3],[2,1]]

heap = []
result = []
time=1
    heap = (4,0)
    result =[0]
time=5
    heap=[(1,2), (3,1)]
    result=[0,2]
time=6
    heap=(3,1)

edge cases:
    empty tasks - excluded
    single task
    multiple tasks enqueued at the same time
    all remaining tasks are alredy enqued 

bugs:
1. while tasks_with_index[i][0] <= current_time and i<len(tasks_with_index): IndexError: list index out of range -- replace condition order
2. File "/box/main.py", line 35, in getOrder     processing_time, index = heapq.heappop(queue) IndexError: index out of range - missed an edge case where last task might finished without next task enqueued
3. [[1,2],[2,4],[3,2],[4,1]] - wrong answer

sort = [[1,2,0], [2,4,1], [3,2,2], 4,1,1]

time=1
    res=[0]
time=3
    q=[(4,1), (2,2)]
"""

        