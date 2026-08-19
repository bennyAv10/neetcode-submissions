"""
Alternatives:
1. sort all array accroding to distance - NlogN
2. Keep max heap of size k and keep pop-push - NlogK (n times updating a)
3. becayse we want all k points and not jsut the Kth point - quick selsect isn't as edfficient

Approach:
1. build a heap of size k - heap element has teh distance + index to original array
2. return the relevant points
Invariant: before processing points[i] with i> k, the heap contains the k closest points to (0, 0)
Preservation: sicne we do pushpop with points[i] we chose between the further point between points[i] and furthest in the heap and throw it, and have the nearer one.
Hence, after processing points[i] the heap still holds the k nearest points
Consequence: when completing prociessing the points list, we have the k nearest points
Time: NLogK
Space: K fot the heap + reesult 
Edge cases:
empty points - excluded
k = 0 - exluded 
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Returns the K points closest to the origin
        """
        def squared_dist(point: list[int]) -> int:
            return point[0]**2 + point[1]**2

        heap = []
        for i in range(len(points)):
            dist = squared_dist(points[i])
            if len(heap) >= k:
               heapq.heappushpop_max(heap, [dist, i])
            else:
                heapq.heappush_max(heap, [dist, i])

        result = []
        for _, index in heap:
            result.append(points[index])

        return result

"""
testing:

points = [[0,2],[2,2]], k = 1

0,2
    dist = 4
    heap = [[4, 0]]

2, 2
    dist = 8
    heap = [[4,0]] # 8 is poped

results = [[0,2]]

"""        