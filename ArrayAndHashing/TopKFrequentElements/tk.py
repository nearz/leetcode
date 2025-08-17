from typing import List


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        maxFreq = 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            maxFreq = max(maxFreq, freq[n])

        buckets = [[] for _ in range(maxFreq + 1)]
        for num, cnt in freq.items():
            buckets[cnt].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

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

    # ANS: [2, 3]
    n = [1, 2, 2, 3, 3, 3]
    k = 2
    res = sol.topKFrequent(n, k)
    print(f"T1: {res}")

    # ANS: [3, 4]
    n = [1, 2, 2, 4, 4, 4, 3, 3, 3]
    k = 2
    res = sol.topKFrequent(n, k)
    print(f"T1: {res}")

    # ANS: [7]
    n = [7, 7]
    k = 1
    res = sol.topKFrequent(n, k)
    print(f"T2: {res}")

    # ANS: [-1]
    n = [-1, -1]
    k = 1
    res = sol.topKFrequent(n, k)
    print(f"T3: {res}")

    # ANS: [1, 2]
    n = [1, 2]
    k = 2
    res = sol.topKFrequent(n, k)
    print(f"T3: {res}")
