from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = len(prices) - 1, len(prices) - 2

        track_max = 0
        while i >= 0 and j >= 0:
            if prices[i] - prices[j] > 0:
                track_max = max(track_max, prices[i] - prices[j])
                j -= 1
            else:
                i = j
                j -= 1

        return track_max

    # NOTE: Time = O(n^2), Space = O(1)
    # def maxProfit(self, prices: List[int]) -> int:
    #     track_max = 0
    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             if prices[i] < prices[j]:
    #                 track_max = max(track_max, prices[j] - prices[i])
    #     return track_max


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 5
    p = [1, 2, 3, 4, 5, 6]
    r = sol.maxProfit(p)
    print(f"T1: {r}")

    # ANS: 6
    p = [10, 1, 5, 6, 7, 1]
    r = sol.maxProfit(p)
    print(f"T1: {r}")

    # ANS: 5
    p = [10, 2, 5, 6, 7, 1]
    r = sol.maxProfit(p)
    print(f"T1: {r}")

    # ANS: 0
    p = [10, 8, 7, 5, 2]
    r = sol.maxProfit(p)
    print(f"T2: {r}")
