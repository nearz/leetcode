from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx, l, r = 0, 0, len(heights) - 1

        while l < r:
            width = r - l
            mn = min(heights[l], heights[r])
            mx = max(mx, width * mn)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return mx


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    h = [1, 7, 2, 5, 4, 7, 3, 6]
    r = sol.maxArea(h)
    print(f"T1: {r}")

    h = [2, 2, 2]
    r = sol.maxArea(h)
    print(f"T2: {r}")
