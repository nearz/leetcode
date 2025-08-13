class Solution:
    # NOTE: time = O(n), space = O(1)
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    # NOTE: time = O(n), space = O(n)
    # def isPalindrome(self, s: str) -> bool:
    #     s = "".join(c for c in s if c.isalnum()).lower()
    #     return s == s[::-1]


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    s = "Was it a car or a cat I saw?"
    r = sol.isPalindrome(s)
    print(f"T1: {r}")

    s = "tab a cat"
    r = sol.isPalindrome(s)
    print(f"T2: {r}")

    s = "race car"
    r = sol.isPalindrome(s)
    print(f"T3: {r}")
