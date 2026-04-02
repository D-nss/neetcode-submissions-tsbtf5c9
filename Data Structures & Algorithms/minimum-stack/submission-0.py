class MinStack:
    # can i call top , pop, getMin before pushing, or on an empty list?
    # i can only push numbers?
    
    # get the min -> of a bynary search?
    # on every push compare, 

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
