from typing import List, Optional

# TODO: Study Binary Search 1 pass.


class Solution:
    # NOTE: Time = O(log(m*n)), Space = O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)
        row: Optional[List[int]] = None
        while top < bottom:
            m = top + (bottom - top) // 2
            if target < matrix[m][0]:
                bottom = m
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                row = matrix[m]
                break

        if row is None:
            return False

        lo, hi = 0, len(row)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if row[m] < target:
                lo = m + 1
            elif row[m] > target:
                hi = m
            else:
                return True

        return False

    # NOTE: Time O(m log n), Space O(1)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # row: Optional[List[int]] = None
    # for m in matrix:
    #     if m[0] <= target and target <= m[-1]:
    #         row = m
    #         break
    #
    # if row is None:
    #     return False
    #
    # print(row)
    # print(target)
    #
    # lo, hi = 0, len(row)
    #
    # while lo < hi:
    #     m = lo + (hi - lo) // 2
    #     if row[m] < target:
    #         lo = m + 1
    #     elif row[m] > target:
    #         hi = m
    #     else:
    #         return True
    #
    # return False


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    m = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    t = 10
    r = sol.searchMatrix(m, t)
    print(f"T1: {r}")

    # m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # t = 3
    # r = sol.searchMatrix(m, t)
    # print(f"T2: {r}")
    #
    # m = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    # t = 15
    # r = sol.searchMatrix(m, t)
    # print(f"T3: {r}")
    #
    # m = [[1]]
    # t = 2
    # r = sol.searchMatrix(m, t)
    # print(f"T4: {r}")
