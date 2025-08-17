class Solution:
    # NOTE: Cleaner
    # NOTE: Time = O(n), Space = O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in parenMap:
                if stack and stack[-1] == parenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

    # def isValid(self, s: str) -> bool:
    #     if len(s) == 0 or len(s) == 1:
    #         return False
    #
    #     stack = []
    #     for c in s:
    #         if c == "(" or c == "[" or c == "{":
    #             stack.append(c)
    #         else:
    #             if not stack:
    #                 return False
    #             p = stack.pop()
    #             if c == ")" and p != "(":
    #                 return False
    #             elif c == "]" and p != "[":
    #                 return False
    #             elif c == "}" and p != "{":
    #                 return False
    #     return True if not stack else False


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: True
    s = "[]"
    b = sol.isValid(s)
    print(f"T1: {b}")

    # ANS: True
    s = "([{}])"
    b = sol.isValid(s)
    print(f"T2: {b}")

    # ANS: False
    s = "[(])"
    b = sol.isValid(s)
    print(f"T3: {b}")

    # ANS: False
    s = "[((])"
    b = sol.isValid(s)
    print(f"T4: {b}")

    # ANS: False
    s = "[(()])"
    b = sol.isValid(s)
    print(f"T4: {b}")

    # ANS: False
    s = "["
    b = sol.isValid(s)
    print(f"T5: {b}")

    # ANS: False
    s = "]]"
    b = sol.isValid(s)
    print(f"T7: {b}")

    # ANS: False
    s = "()]"
    b = sol.isValid(s)
    print(f"T8: {b}")

    # ANS: False
    s = "((("
    b = sol.isValid(s)
    print(f"T9: {b}")
