"""
Alternatives:
1. sort (linear backet sort). find the most frquent task time (call the count t) - the reuiqred time (t-1) (n+1) +num-of-max-characters (i.e. how many tasks are the most freuqnet)
or the total number of taks - the max between both options
2. max heap and queue - every time you take take from the heap and put into the queue or from the queue if it's already alowned 
This time I'm going with heap and queue to practice it - both solutions are linear
Invariant: at cpu cycle i we have a valid and optimal arragenemt of cycles 0..i-1. with max heap by remaining cycles per tasks and queue for tasks that were not allowed before i
preservation: by assigning cycle i to either the heap or the queue (if queue is allowed) - depends which one has higher remaning cycles the assignment 0...i is an optimal and valid assignment
Consequence: when i=len(tasks) we have a valid assignment
Time: heap is const (26 tasks types) so total time is linear (len(tasks))
space: heap size is constant, queue the same. 
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_to_count = collections.Counter(tasks)
        heap = [[count, task, -1] for task, count in tasks_to_count.items()]
        heapq.heapify_max(heap)
        queue = collections.deque()

        current_assignment = 0 
        while heap or queue:
            if queue and queue[0][2] + n < current_assignment:
                heapq.heappush_max(heap, queue.popleft())
            
            if heap:
                current_task = heapq.heappop_max(heap)
                current_task[0]-=1
                if current_task[0] > 0:
                    current_task[2] = current_assignment
                    queue.append(current_task) 
            
            # with queue but no heap, we assign idle cycle
            current_assignment += 1

        return current_assignment

"""
example 1:
["X","X","Y","Y"], n = 2

heap [[2, X, -1], [2, Y, -1]]
q = []

current = 0
    heap = [2, Y, -1]
    q = [1, X, 0]
c=1
    heap []
    q = [[1,x,0], [1,y,1]]
c=2
    # 0+2 not enough --> idle
c=3
    # x moves to heap
    # x pulled from heap
    finished x tasks
c = 4
    y moves to heap
    y extracted from heap
    y is zero

c=5

return 5


"""
        