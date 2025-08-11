from typing import List

# TODO: Revist this after watching Neetcode video.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


    # NOTE: O(n log n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = {}
    #     for n in nums:
    #         freq[n] = freq.get(n, 0) + 1
    #
    #     arr = []
    #     for num, cnt in freq.items():
    #         arr.append([cnt, num])
    #     arr.sort()
    #
    #     res = []
    #     while len(res) < k:
    #         res.append(arr.pop()[1])
    #
    #     return res

    # NOTE: O(n * k)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = {}
    #     for n in nums:
    #         freq[n] = freq.get(n, 0) + 1
    #
    #     res = []
    #     c = 0
    #     while c < k:
    #         max = 0
    #         i = 0
    #         for key, v in freq.items():
    #             if v > max:
    #                 max = v
    #                 i = key
    #
    #         res.append(i)
    #         freq.pop(i)
    #         c += 1
    #
    #     return res


if __name__ == "__main__":
    sol = Solution()

    n = [1, 2, 2, 3, 3, 3]
    k = 2
    res = sol.topKFrequent(n, k)
    print(f"T1: {res}")

    n = [7, 7]
    k = 1
    res = sol.topKFrequent(n, k)
    print(f"T2: {res}")
