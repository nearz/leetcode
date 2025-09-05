from typing import List
import heapq


# NOTE: Time = O(nlogk), Space = O(k), k is size of tracker
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        print(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    print("MAIN:")

    kl = KthLargest(3, [1, 2, 3, 3])
    adds = [3, 5, 6, 7, 8]
    res = []
    for a in adds:
        res.append(kl.add(a))
    print(f"T1: {res}")
