class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        popItem = self.list.pop()
        if len(self.list) == 0:
            self.min = None
        elif popItem == self.min:
            self.min = min(self.list)

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # return min(self.list)
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
