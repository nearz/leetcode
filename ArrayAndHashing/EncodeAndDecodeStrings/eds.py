from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        bck = 0
        while i < len(s):
            if s[i] == "#":
                n = int(s[bck:i])
                ss = s[i + 1 : i + n + 1]
                res.append(ss)
                i = i + n + 1
                bck = i
            else:
                i += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    n = ["neet", "code", "love", "you"]
    e = sol.encode(n)
    print(f"TE1: {e}")
    d = sol.decode(e)
    print(f"TD1: {d}")

    n = ["we", "say", ":", "yes"]
    e = sol.encode(n)
    print(f"TE1: {e}")
    d = sol.decode(e)
    print(f"TD1: {d}")
