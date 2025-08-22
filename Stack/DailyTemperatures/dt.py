from typing import List


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        i = len(temperatures) - 1
        stack = []
        while i >= 0:
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                i -= 1
            elif temperatures[i] >= stack[-1][0]:
                stack.pop()
            else:
                res[i] = stack[-1][1] - i
                stack.append((temperatures[i], i))
                i -= 1

        return res

    # NOTE: Time = O(n^2), Space = O(n)
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(temperatures)):
    #         if i == len(temperatures) - 1:
    #             res.append(0)
    #         else:
    #             for j in range(i + 1, len(temperatures)):
    #                 if temperatures[i] < temperatures[j]:
    #                     res.append(j - i)
    #                     break
    #                 elif j == len(temperatures) - 1:
    #                     res.append(0)
    #
    #     return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    t = [30, 38, 30, 36, 35, 40, 28]
    r = sol.dailyTemperatures(t)
    print(f"T1: {r}")

    t = [22, 21, 20]
    r = sol.dailyTemperatures(t)
    print(f"T1: {r}")
