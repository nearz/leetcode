from typing import Optional

# TODO: Note sure I like the nonlocal. Can I pass a collection var?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass

    def _dfs(self, root: Optional[TreeNode], diam int) -> int:
        pass

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     res = 0
    #
    #     def dfs(root: Optional[TreeNode]) -> int:
    #         nonlocal res
    #         if not root:
    #             return 0
    #         lh = dfs(root.left)
    #         rh = dfs(root.right)
    #         res = max(res, lh + rh)
    #         return 1 + max(lh, rh)
    #
    #     dfs(root)
    #     return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    root.right = two
    two.left = three
    two.right = four
    three.left = five
    res = sol.diameterOfBinaryTree(root)
    print(f"T1: {res}")

    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    root.right = two
    two.left = three
    two.right = four
    three.left = five
    four.right = six
    res = sol.diameterOfBinaryTree(root)
    print(f"T1: {res}")
