from typing import List

# TODO: By Division should meet time/space goals, but see videos for Prefix & Suffix. I am not sure what they are.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zCnt = 0
        zi = 0
        for i, n in enumerate(nums):
            if n == 0:
                zCnt += 1
                if zCnt == 1:
                    zi = i
                continue
            total *= n

        if zCnt == 1:
            res = [0] * len(nums)
            res[zi] = total
            return res
        if zCnt > 1:
            return [0] * len(nums)

        return [total // n for n in nums]

    # NOTE: Brute Force, time = O(n^2)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         p = 1
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             p *= nums[j]
    #         res.append(p)
    #
    #     return res


if __name__ == "__main__":
    sol = Solution()

    n = [1, 2, 4, 6]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [-1, 0, 1, 2, 3]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [1, 0, 2, 4, 0, 6]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [0, 0]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")

    n = [1, 2]
    r = sol.productExceptSelf(n)
    print(f"T1: {r}")
