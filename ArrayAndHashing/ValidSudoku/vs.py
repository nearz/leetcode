from typing import List


class Solution:
    # NOTE: Brute force
    # TODO: Not clear on time, always fixed input so time = O(1)?
    # TODO: May be cleaner ways to do this.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for j in i:
                if j == ".":
                    continue
                if j in seen:
                    return False
                seen.add(j)

        for i in range(9):
            seen = set()
            for j in board:
                if j[i] == ".":
                    continue
                if j[i] in seen:
                    return False
                seen.add(j[i])

        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (box // 3) * 3 + i
                    c = (box % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True


if __name__ == "__main__":
    sol = Solution()

    b = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    r = sol.isValidSudoku(b)
    print(f"T1: {r}")

    b = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    r = sol.isValidSudoku(b)
    print(f"T1: {r}")
