from typing import List
import heapq


class Solution:
    # NOTE: Time = O(n + m), Space = O(m), n len of input, m is max stone
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1

            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first

    # NOTE: Time = O(nlogn), Space = O(n)
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     stones = [-s for s in stones]
    #     heapq.heapify(stones)
    #
    #     while len(stones) > 1:
    #         y = abs(heapq.heappop(stones))
    #         x = abs(heapq.heappop(stones))
    #         if x < y:
    #             new_weight = y - x
    #             heapq.heappush(stones, -new_weight)
    #
    #     if len(stones) == 1:
    #         return abs(stones[0])
    #     return 0


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 1
    s = [2, 3, 6, 2, 4]
    res = sol.lastStoneWeight(s)
    print(f"T1: {res}")

    # ANS: 1
    s = [1, 2]
    res = sol.lastStoneWeight(s)
    print(f"T2: {res}")

    # ANS: 0
    s = [1, 1, 1, 1]
    res = sol.lastStoneWeight(s)
    print(f"T3: {res}")

    # ANS: 1
    s = [1, 1, 1, 1, 1]
    res = sol.lastStoneWeight(s)
    print(f"T3: {res}")
