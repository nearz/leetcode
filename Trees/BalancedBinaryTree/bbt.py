from typing import Optional

# TODO: Note sure I like the nonlocal. Can I pass a collection var?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)
            diff = abs(lh - rh)
            if diff > 1:
                res = False

            return 1 + max(lh, rh)

        dfs(root)
        return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    root.left = two
    root.right = three
    three.left = four
    res = sol.isBalanced(root)
    print(f"T1: {res}")

    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    root.left = two
    root.right = three
    three.left = four
    four.left = five
    res = sol.isBalanced(root)
    print(f"T1: {res}")
