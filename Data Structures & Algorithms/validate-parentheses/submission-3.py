"""
assumptions:
only brackets\parenthesis 3 styles characers - but i can just ignore any other character

rule:
push opening into a stack. when there is closing, the last opening must be the same type
closing with no matching opening is invalid
orphan opening is invalid

have a stack push openings and on closings check the correct openings

on finishing iteration verify openings stack is empty

N - str length
Time Complexity: O(N)
space O(N)

missed edge case of closing only in the input
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """Verifies strings with parenthessis is valid
        """

        stack = collections.deque()
        closing_to_opening = {')' : '(', '}': '{' ,']': '['}

        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            elif c in closing_to_opening:
                if not stack or closing_to_opening[c] != stack.pop():
                    return False

        return not stack
        