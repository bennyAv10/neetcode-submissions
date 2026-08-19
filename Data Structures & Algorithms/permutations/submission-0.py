"""
Approach: recusrively visit any unvisited number. On each visit you iterate through the array across all unvisited indices
[1,2,3]

[]
 [1]
    [1,2]
        [1,2,3]
    [1,3]
 [2]
 [3]

 when you reach the leaf (visited is size of nums) - you add teh results

 Invariant: before visiting the  level k+1, all the prefixes from the recusrion hurarchey are all possible permutation prefixes of len k
 Preservation: each prefix create all possible next place - together creating all prefixes of len k+1
 Consequence: at level n we have all permutations
 Time and space Complexity: N factorail (Number of permutations)
Note recursion is valid here as size <=6 recursion depth is n
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        return all permutations of `nums`
        """
        def permute_visit(visited_indices: set[int], prefix: list[int], results: list[list[int]]):

            if len(prefix) == len(nums):
                results.append(prefix.copy())
                return
            
            for i in range(len(nums)):
                if i in visited_indices:
                    continue

                visited_indices.add(i)
                prefix.append(nums[i])

                permute_visit(visited_indices, prefix, results)

                visited_indices.remove(i)
                prefix.pop()
        
        results = []
        permute_visit(set(), [], results)

        return results

"""
[1,2,3]

{}, [], []
    [1]
        [1,2]
            [1,2,3]
        [1,3]

    [2]
    [3]
"""