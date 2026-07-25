class MinStack:

    def __init__(self):
        self.stack=[]

        self.min_val = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            self.min_val.append(min(self.min_val[-1], val))

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_val[-1]


    def top(self) -> int:
        if not self.stack:
            return 0
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

