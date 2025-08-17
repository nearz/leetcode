class MinStack:
    def __init__(self):
        self.min = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

    def printStack(self) -> None:
        print(self.stack)


if __name__ == "__main__":
    print("MAIN:")
    ms = MinStack()
    ms.push(1)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
    ms.push(2)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
    ms.push(-1)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
    ms.push(-5)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
    ms.push(-2)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
    ms.push(-6)
    ms.printStack()
    print(ms.top())
    print(ms.getMin())
