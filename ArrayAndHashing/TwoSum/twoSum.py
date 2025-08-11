from typing import List


class Solution:
    # NOTE: a little cleaner
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracker:
                return [tracker[diff], i]
            tracker[n] = i
        return []

    # NOTE: time = O(n)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     tracker = {}
    #     final = []
    #     for i, n in enumerate(nums):
    #         j = tracker.get(target - n, None)
    #         if j != None:
    #             final.extend([j, i])
    #             break
    #         tracker[n] = i
    #     return final


if __name__ == "__main__":
    sol = Solution()

    s = [2, 7, 11, 15]
    t = 9
    r = sol.twoSum(s, t)
    print(f"T1: {r}")

    s = [4, 5, 6]
    t = 10
    r = sol.twoSum(s, t)
    print(f"T2: {r}")

    s = [5, 5]
    t = 10
    r = sol.twoSum(s, t)
    print(f"T3: {r}")
