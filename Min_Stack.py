from collections import deque

class MinStack(object):
    def __init__(self):
        self.s = deque()
        self.aux = deque()

    def push(self, val):
        
        self.s.append(val)
        if not self.aux:
            self.aux.append(val)
        else:
            if self.aux[-1] >= val:
                self.aux.append(val)
    def isEmpty(self):
        return not self.s
 
        

    def pop(self):
        if self.isEmpty():
            print('Stack underflow')
            exit(-1)
        top = self.s.pop()
        if top == self.aux[-1]:
            self.aux.pop()

        return top
        
        
        

    def top(self):
        return self.s[-1]

    def getMin(self):
        if not self.aux:
            print('Stack underflow')
            exit(-1)
        return self.aux[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
