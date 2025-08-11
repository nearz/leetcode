from typing import List

# TODO: Better solution, time = O(n). See Neetcode.


class Solution:
    # NOTE: Brute Force, time = O(n^2)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                p *= nums[j]
            res.append(p)

        return res


if __name__ == "__main__":
    sol = Solution()

    n = [1, 2, 4, 6]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [-1, 0, 1, 2, 3]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [0, 0]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")
