"""
convert to pairs (position, speed) and sort in decending order.
iterate and for each i the next cars can only come later but not earlier
i.e. a car started at a lower position can only arrive after any car started
time: O(Nlogn) soring + a single pass
space: N for positions and speeds
constrans: N (cars) <= 100k --> nlogN ~=5*10^5 which is fine and space is 10^5 * 8 bytes ~= 1mb

edge cases:
connecting just before target
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_speed.sort(reverse=True)

        latest_arrival = -1

        count=0

        for i in range (len(position_speed)):
            cp, cs = position_speed[i] # current_position, current_speed
            # e.g. 7 miles left at 3 speed --> will arrive at 7/3
            current_arrival= (target-cp)/cs
            if current_arrival >latest_arrival:
                latest_arrival = current_arrival
                count+=1
        
        return count


"""
target = 10, position = [4,1,0,7], speed = [2,2,1,1]


(7, 1), (4,2), (1,2), (0, 1), , 

count=0

(7,1)
    ca=3
    la=3
    c=1
(4,2)
    ca=3
(1,2)
    ca=4.5
    la=4.5
    c=2
(0,1)
    ca=10
    la=10
    c=3

bug 1: 
"""