class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    print("MAIN:")
    # minStack = MinStack()
    # minStack.push(1)
    # minStack.push(2)
    # minStack.push(0)
    # print(minStack.getMin())
    # minStack.pop()
    # print(minStack.top())
    # print(minStack.getMin())

    ms = MinStack()
    ms.push(-1)
    ms.push(5)
    ms.push(0)
    ms.push(-5)
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    ms.push(4)
    ms.push(-4)
    ms.push(2)
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
    ms.pop()
    print(ms.getMin())
