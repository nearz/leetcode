from typing import List


class Solution:
    # Use 1 Indexing.
    # NOTE: Always think about negative int values
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        l, r = 0, len(numbers) - 1
        while l < r:
            n = numbers[l] + numbers[r]
            if n == target:
                return [l + 1, r + 1]
            elif n > target:
                r -= 1
            else:
                l += 1

        return []


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: [1, 2]
    n = [1, 2, 3, 4]
    r = sol.twoSum(n, 3)
    print(f"T1: {r}")

    # ANS: [1, 3]
    n = [1, 2, 3, 4]
    r = sol.twoSum(n, 4)
    print(f"T2: {r}")

    # ANS: [2, 3]
    n = [2, 4, 5, 6, 8, 11, 15, 16]
    r = sol.twoSum(n, 9)
    print(f"T3: {r}")

    # ANS: [1, 2]
    n = [-1, 0]
    r = sol.twoSum(n, -1)
    print(f"T4: {r}")

    # ANS: [1, 3]
    n = [-5, -3, 0, 1, 2]
    r = sol.twoSum(n, -5)
    print(f"T5: {r}")

    # ANS: [2, 3]
    n = [-5, -3, -2, 1, 2]
    r = sol.twoSum(n, -5)
    print(f"T6: {r}")

    # ANS: [3, 6]
    n = [-5, -3, -2, 0, 1, 2]
    r = sol.twoSum(n, 0)
    print(f"T7: {r}")
