from typing import List


class Solution:

    # NOTE: Simplified further
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    # NOTE: Cleaner approach
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     seen = set()
    #     for n in nums:
    #         if n in seen:
    #             return True
    #         seen.add(n)
    #     return False

    # NOTE: Original solution
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     freq = {}
    #     for n in nums:
    #         if n not in freq:
    #             freq[n] = 1
    #         else:
    #             freq[n] += 1
    #
    #     for _, v in freq.items():
    #         if v > 1:
    #             return True
    #
    #     return False


if __name__ == "__main__":
    s = Solution()
    n1 = [1, 2, 3, 3]
    print(s.hasDuplicate(n1))

    n2 = [1, 2, 3, 4]
    print(s.hasDuplicate(n2))

    n3 = []
    print(s.hasDuplicate(n3))
