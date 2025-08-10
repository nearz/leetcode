from collections import defaultdict
from typing import List


class Solution:
    # NOTE: Time O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            hash = [0] * 26
            for c in s:
                hash[ord(c) - ord("a")] += 1
            res[tuple(hash)].append(s)
        return list(res.values())

    # NOTE: O(m * n log n)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         sortedS = "".join(sorted(s))
    #         res[sortedS].append(s)
    #     print(res)
    #     return list(res.values())

    # NOTE: Brute force, O(n^2 * k)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     l = len(strs)
    #     seen = set()
    #     final = []
    #     for i in range(l):
    #         if strs[i] in seen:
    #             continue
    #         group = [strs[i]]
    #         for j in range(l):
    #             if i == j:
    #                 continue
    #             if isAnagram(strs[i], strs[j]):
    #                 seen.add(strs[j])
    #                 group.append(strs[j])
    #         final.append(group)
    #         group = []
    #
    #     return final


# NOTE: For Brute force method
# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     freq = [0] * 26
#     for cs, ct in zip(s, t):
#         freq[ord(cs) - ord("a")] += 1
#         freq[ord(ct) - ord("a")] -= 1
#
#     return all(f == 0 for f in freq)


if __name__ == "__main__":
    sol = Solution()

    s = ["act", "pots", "tops", "cat", "stop", "hat"]
    f = sol.groupAnagrams(s)
    print(f"T1: {f}")

    s = ["x"]
    f = sol.groupAnagrams(s)
    print(f"T2: {f}")

    s = [""]
    f = sol.groupAnagrams(s)
    print(f"T3: {f}")
