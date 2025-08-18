from typing import List


class Solution:
    # NOTE: Recursion
    # def search(self, nums: List[int], target: int) -> int:
    #     return self.binary_search(0, len(nums), nums, target)
    #
    # def binary_search(self, lo: int, hi: int, nums: List[int], target: int) -> int:
    #     if lo > hi:
    #         return -1
    #     m = lo + (hi - lo) // 2
    #
    #     if nums[m] == target:
    #         return m
    #     if nums[m] < target:
    #         return self.binary_search(m + 1, hi, nums, target)
    #     return self.binary_search(lo, m - 1, nums, target)

    # NOTE: [l, r] inclusive
    # def search(self, nums: List[int], target: int) -> int:
    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     # NOTE: Python would handle (l+r)//2 but below would keep overflow from occuring in other langs
    #     m = l + ((r - l) // 2)
    #     if nums[m] < target:
    #         l = m + 1
    #     elif nums[m] > target:
    #         r = m - 1
    #     else:
    #         return m
    # return -1

    # NOTE: Time O(logn) log2n = x, n = 16, x = 4, div 16 by 2 4 times 4 total iterations
    # NOTE: Space O(1)
    # NOTE: [l, r) half-open interval
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1

        return -1


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    n = [-1, 0, 2, 4, 6, 8]
    t = 4
    r = sol.search(n, t)
    print(f"T1: {r}")

    n = [-1, 0, 2, 4, 6, 8]
    t = 2
    r = sol.search(n, t)
    print(f"T1: {r}")

    n = [-1, 0, 2, 4, 6, 8]
    t = 3
    r = sol.search(n, t)
    print(f"T1: {r}")

    n = [-1, 0, 3, 5, 9, 12]
    t = 9
    r = sol.search(n, t)
    print(f"T1: {r}")
