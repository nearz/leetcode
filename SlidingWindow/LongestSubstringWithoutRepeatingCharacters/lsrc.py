class Solution:
    # NOTE: Time = O(n^3), Space = O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        track_max = 0
        for k in range(len(s)):
            i = 0
            j = 1 + k
            while i < len(s) and j <= len(s):
                if not self.duplicates(s[i:j]):
                    track_max = max(track_max, j - i)
                i += 1
                j += 1

        return track_max

    def duplicates(self, sub: str) -> bool:
        seen = set()
        for s in sub:
            if s in seen:
                return True
            seen.add(s)
        return False


if __name__ == "__main__":
    """
    abcd
    a-b-c-d
    ab-bc-cd
    abc-bcd
    abcd

    abc
    a-b-c
    ab-bc
    """
    print("MAIN:")
    sol = Solution()

    # ANS: 3
    s = "zxyzxyz"
    r = sol.lengthOfLongestSubstring(s)
    print(f"T1: {r}")

    # ANS: 1
    s = "xxxx"
    r = sol.lengthOfLongestSubstring(s)
    print(f"T2: {r}")

    # ANS: 4
    s = "abcd"
    r = sol.lengthOfLongestSubstring(s)
    print(f"T3: {r}")

    # ANS: 2
    s = "xzzzy"
    r = sol.lengthOfLongestSubstring(s)
    print(f"T4: {r}")

    # ANS: 3
    # s = "abbcdaad"
    # r = sol.lengthOfLongestSubstring(s)
    # print(f"T5: {r}")
