#155. Min Stack
# Nothing to say
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> None:
        del self.stack[len(self.stack)-1]
        return

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if self.stack==null:
            minnum=0
        else:
            minnum=self.stack[0]
        for i in self.stack:
            if i<minnum:
                minnum=i
        return minnum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Runtime: 1832 ms, faster than 5.02% of Python3 online submissions for Min Stack.
#Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Min Stack.