from typing import List

# TODO: Need to revisit


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        return [[1]]


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    n = [-1, 0, 1, 2, -1, -4]
    r = sol.threeSum(n)
    print(f"T1: {r}")

    # n = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    # r = sol.threeSum(n)
    # print(f"T1: {r}")
    #
    # n = [-1, 0, 1, 7, -1, -4]
    # r = sol.threeSum(n)
    # print(f"T1: {r}")
    #
    # n = [-1, 0, 1]
    # r = sol.threeSum(n)
    # print(f"T1: {r}")
    #
    # n = [0, 1, 1]
    # r = sol.threeSum(n)
    # print(f"T1: {r}")
