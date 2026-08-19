closings = {']':'[', ')': '(', '}':'{'}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in closings:
                expected_opening = closings[c]
                if stack and stack.pop() == expected_opening:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack

        
        