from typing import List


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oprts = {"+", "-", "*", "/"}

        for t in tokens:
            if t in oprts:
                b = stack.pop()
                a = stack.pop()
                res = self._calc(a, b, t)
                stack.append(res)
            else:
                stack.append(int(t))
            print(stack)

        return stack.pop()

    def _calc(self, a: int, b: int, op: str) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            return int(a / b)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 5
    tks = ["1", "2", "+", "3", "*", "4", "-"]
    r = sol.evalRPN(tks)
    print(f"T1: {r}")

    # ANS: 22
    tks = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    r = sol.evalRPN(tks)
    print(f"T2: {r}")
