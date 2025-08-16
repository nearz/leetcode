from typing import List

# TODO: Need to revisit


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        i = 0
        while i <= len(nums) - 2:
            j = len(nums) - 1
            while j > i + 1:
                if nums[i] + nums[i + 1] + nums[j] == 0:
                    res.append([nums[i], nums[i + 1], nums[j]])
                j -= 1
            i += 1

        return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    n = [-1, 0, 1, 2, -1, -4]
    r = sol.threeSum(n)
    print(f"T1: {r}")
