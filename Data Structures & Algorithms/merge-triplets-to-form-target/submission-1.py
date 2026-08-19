"""
Approach: for any triplet, if ai>x or bi>y or ci>j it can't be used any more. also triplets with none of a, b, or c are the target value can be discarded
with ther rest (For the next part i had to read the hint), if the x or y or z appears in any triplet since the rest are <= than target max operation 
will take the desired component
Invariant: before processing the ith triplet, we have some discarded triplets (either has some bigger than target value or no target value),
and some with one of a, b, c equals to target with the rest coordinates lower
Preservation: after processing Ith element it's either discarded or has one lement equals to target with the rest lower than target
Consequence: when done processing all the triplets, we can get the target IIF all targets are covered among all triplets
Time: O(N)
Space: O(1)

"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """Checks if repeating triplets merge by max operation can generate the target triplet
        """
        x_found=False
        y_found=False
        z_found=False
        for (a,b,c) in triplets:
            if a > target[0] or b>target[1] or c>target[2]:
                continue
            
            if a == target[0]:
                x_found = True
            if b == target[1]:
                y_found = True
            if c == target[2]:
                z_found = True
        
        return x_found and y_found and z_found

"""
 triplets = [[1,2,3],[7,1,1]], target = [7,2,3]

 1,2,3

 y-found
 z-found

 7,1,1
 x-found


 adverserial cases:
 triplet is target 

"""



        