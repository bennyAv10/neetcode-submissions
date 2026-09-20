"""
Brute force: starts with k=1, ..., max(piles) (h>= len). for each k run through the array (O(h) steps). you stop after spending h hours return the first speed in which you can finish - 
    Time: max(piles)*N (N=len piles) - with the given constrains this is 10^9 * 10^4 ~= 10^13 --> too much

binary search: over the solution space - the space is montonous --> if P(k)=true (can finish in <=h) then for each l>k p(l) is true. starts with lo=1, hi=max(pile)
for a given k, you calculate if can finish in k (Time: N) - Total time log(max(pile)) * N - with N=10k and max(pile)=1b ~= 10k*9
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed: int):
            time_spent=0
            for pile in piles:
                time_spent += math.ceil(pile/speed)
                if time_spent>h:
                    return False
            
            return True
        
        lo=1
        hi=max(piles)

        while lo<hi:
            mid = (lo+hi)//2

            if canFinish(mid):
                hi = mid
            else:
                lo = mid+1

        return lo


"""
lo =3 , hi =4
mid = 3
    yes --> hi=3 --> lo=hi=right answer
    noo --> lo=4 --> lo=hi=right answer


lo=3, hi =5
mid = 4
    yes --> hi=4, lo=3 --> back to first case
    no --> lo=5, hi=5
"""