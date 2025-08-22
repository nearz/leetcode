from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < nums[r]:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 4
    n = [1, 2, 3, 4, 5, 6]
    t = 5
    r = sol.search(n, t)
    print(f"T1: {r}")

    # ANS: 0
    n = [5, 6, 1, 2, 3, 4]
    t = 5
    r = sol.search(n, t)
    print(f"T2: {r}")

    # ANS: 1
    n = [6, 1, 2, 3, 4, 5]
    t = 1
    r = sol.search(n, t)
    print(f"T3: {r}")

    # ANS: 3
    n = [5, 6, 1, 2, 3, 4]
    t = 2
    r = sol.search(n, t)
    print(f"T4: {r}")

    # ANS: 4
    n = [3, 4, 5, 6, 1, 2]
    t = 1
    r = sol.search(n, t)
    print(f"T5: {r}")

    # ANS: -1
    n = [3, 4, 5, 6, 1, 2]
    t = 7
    r = sol.search(n, t)
    print(f"T6: {r}")

    # ANS: 0
    n = [3, 5, 6, 0, 1, 2]
    t = 3
    r = sol.search(n, t)
    print(f"T7: {r}")
