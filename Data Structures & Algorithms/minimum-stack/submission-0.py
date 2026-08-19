"""
stack in O(n) is with dequeue. you append and pop in O(1)

get min
option a: search for min each time - O(n)

option b: keep a sorted copy

invariant: min can only change in push (the new item might be the new min) or pop (older min).
we can just have another stack just with mins

mins_stack --> push items where a new item <= min. pop when popped item == min

the example in the left

push 1
[1]
[1]
push 2
[1,2]
[1] (2>1 the current min)
push 0
[1,2,0]
[1,0]
get min -->0
pop
[1,2]
[1] - val=0 ==mins[-1]

top --> 2

get min 1

time for deque is 1 (implementation is blocks of memory no need to copy on resize)
space is <=2N
"""
class MinStack:

    def __init__(self):
        self._stack = collections.deque()
        self._mins_stack = collections.deque()
        

    def push(self, val: int) -> None:
        self._stack.append(val)

        # this smaller or equal to min or stack is empty
        if not self._mins_stack or val <= self._mins_stack[-1]:
            self._mins_stack.append(val)
    
    def pop(self) -> None:
        val = self._stack.pop()

        if val == self._mins_stack[-1]:
            self._mins_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._mins_stack[-1]
        
