class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26
        for cs, ct in zip(s, t):
            freq[ord(cs) - ord("a")] += 1
            freq[ord(ct) - ord("a")] -= 1

        return all(f == 0 for f in freq)

    # NOTE: Meets time: O(n + m), space: O(1)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     s_freq = {}
    #     for c in s:
    #         s_freq[c] = s_freq.get(c, 0) + 1
    #
    #     t_freq = {}
    #     for c in t:
    #         t_freq[c] = t_freq.get(c, 0) + 1
    #
    #     for k, v in s_freq.items():
    #         in_t = t_freq.get(k, 0)
    #         if in_t <= 0 or in_t != v:
    #             return False
    #
    #     return True

    # NOTE: Not O(n+m) as suggested in Neetcode problem
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()

    s = "racecar"
    t = "carrace"
    b = sol.isAnagram(s, t)
    print(f"T1: {b}")

    s = "jar"
    t = "jam"
    b = sol.isAnagram(s, t)
    print(f"T2: {b}")

    s = "xx"
    t = "x"
    b = sol.isAnagram(s, t)
    print(f"T3: {b}")

    s = "a"
    t = "ab"
    b = sol.isAnagram(s, t)
    print(f"T2: {b}")
