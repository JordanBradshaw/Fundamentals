# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#    push(x) -- Push element x onto stack.
#    pop() -- Removes the element on top of the stack.
#    top() -- Get the top element.
#    getMin() -- Retrieve the minimum element in the stack.


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackList = []

    def push(self, x: int) -> None:
        self.stackList.append(x)

    def pop(self) -> None:
        if self.stackList:
            self.stackList.pop()

    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return min(self.stackList)


jar = MinStack()
jar.push(1)

# Runtime: 584 ms, faster than 21.17% of Python3 online submissions for Min Stack.
# Memory Usage: 17.9 MB, less than 64.69% of Python3 online submissions for Min Stack.
