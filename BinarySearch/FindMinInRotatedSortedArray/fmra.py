from typing import List

# TODO: Review


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            print(f"l: {l}, m: {m}, r: {r}")
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    n = [1, 2, 3, 4, 5, 6]
    r = sol.findMin(n)
    print(f"T1: {r}")

    n = [6, 1, 2, 3, 4, 5]
    r = sol.findMin(n)
    print(f"T1: {r}")

    n = [4, 5, 6, 1, 2, 3]
    r = sol.findMin(n)
    print(f"T1: {r}")
