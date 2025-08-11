from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return 0

    # NOTE: time = O(n + k), space = O(k)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #
    #     maxMag = nums[0]
    #     for n in nums:
    #         n = abs(n)
    #         maxMag = max(n, maxMag)
    #
    #     track = [0] * (maxMag * 2 + 3)
    #     midZero = len(track) // 2
    #     for n in nums:
    #         if n < 0:
    #             n = abs(n)
    #             n = midZero - n
    #             track[n] += 1
    #         else:
    #             n = midZero + n
    #             track[n] += 1
    #
    #     track.append(0)
    #     maxConsecutive = 0
    #     count = 0
    #     for n in track:
    #         if n > 0:
    #             count += 1
    #         else:
    #             if count > maxConsecutive:
    #                 maxConsecutive = count
    #             count = 0
    #
    #     return maxConsecutive


if __name__ == "__main__":
    sol = Solution()

    # ANS: 4
    n = [2, 20, 4, 10, 3, 4, 5]
    a = sol.longestConsecutive(n)
    print(f"T1: {a}")

    # ANS: 7
    n = [0, 3, 2, 5, 4, 6, 1, 1]
    a = sol.longestConsecutive(n)
    print(f"T2: {a}")

    # ANS: 5
    n = [-5, -2, -1, 0, 1, 2, 5]
    a = sol.longestConsecutive(n)
    print(f"T2: {a}")

    # ANS: 0
    n = []
    a = sol.longestConsecutive(n)
    print(f"T2: {a}")
