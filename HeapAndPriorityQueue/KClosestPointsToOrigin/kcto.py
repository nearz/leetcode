from typing import List
import math, heapq

# TODO: Quick Select, O(n) avg case. Take a look


class Solution:
    # NOTE: Time = O(k * logn), Space = O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            d = self._distance_from_origin(p[0], p[1])
            heapq.heappush(heap, (d, p))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def _distance_from_origin(self, x: int, y: int) -> float:
        return math.sqrt((x**2) + (y**2))


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    p = [[0, 2], [2, 2]]
    res = sol.kClosest(p, 1)
    print(f"T1: {res}")

    p = [[0, 2], [2, 0], [2, 2]]
    res = sol.kClosest(p, 2)
    print(f"T2: {res}")

    p = [[3, 3], [5, -1], [-2, 4]]
    res = sol.kClosest(p, 2)
    print(f"T3: {res}")
