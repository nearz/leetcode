from typing import List


class Solution:

    # NOTE: Time = O(n), Space = O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        cnt = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                cnt = max(length, cnt)
        return cnt

    # NOTE: Time = O(n log n) assuming sort i O(nlogn), Space = O(1) or O(n) depends on sort.
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     elif len(nums) == 1:
    #         return 1
    #
    #     nums.sort()
    #
    #     cnt = 1
    #     maxCnt = 1
    #
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             continue
    #         elif nums[i] + 1 == nums[i + 1]:
    #             cnt += 1
    #             maxCnt = max(maxCnt, cnt)
    #         else:
    #             cnt = 1
    #
    #     return maxCnt

    # NOTE: time = O(n + k), space = O(k)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
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
