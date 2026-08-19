"""
Approach: this is djakstra (shortest weighted path) + find the max time out of all nodes
Invariant: when popping a node from the heap (priority queue), the fastest way to reach it from source is the smaller of either the recorded dist oar the popped distance
Preservation: when we popped its neightbors (in cases the popped distance was shorter), it's still true - we eitehr had already a shorter way to reach them or this is the shortest.
Otherwise, i.e. unexplored way is shorter, since all weights are positive we'd already reach that before
Consequence: since the invariant is true about the baseline (only source with distance 0 - rest is inf), we find the shortest path for each node from the given soruce. findding the max dist 
gives the answer
Time: there are upto V in the heap at any given time, and we push\pop every edge - O(V +(E*logV))
Space: O(V)

"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for source, dest, dist in times:
            graph[source-1].append([dest-1, dist]) # converting from 1-index to 0-index
        dist = [float('inf') for i in range(n)]


        heap = [(0, k-1)]

        while heap:
            current_distance, node = heapq.heappop(heap)
            if current_distance > dist[node]:
                continue
            
            dist[node] = current_distance
            for dest, dest_dist in graph[node]:
                if current_distance+dest_dist < dist[dest]:
                    heapq.heappush(heap, (current_distance+dest_dist, dest))
                    dist[dest] = current_distance+dest_dist

        res = max(dist)
        return int(res) if res != float('inf') else -1

"""
test

Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

graph

0: (1, 1), (3,4) 
1: (2,1)
2: (3,1)
3

heap = [(0,k)]

0,k
    d --> k:0
    heap --> (1,1), (4,3)

1, 1
    d --> 1: 1
    heap --> (2, 2)

2, 2
    d --> 2: 2
    heap --> (3, 3)

3, 3
    d --> 3: 3

4, 3
    continue --> we already got to 3
"""



