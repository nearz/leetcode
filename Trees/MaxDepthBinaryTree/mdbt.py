from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n), Space = O(h), cleaner
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # NOTE: Time = O(n), Space = O(h)
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     return self._count_depth(root, 1)
    #
    # def _count_depth(self, node: Optional[TreeNode], depth: int) -> int:
    #     if not node:
    #         return depth - 1
    #     left_depth = self._count_depth(node.left, depth + 1)
    #     right_depth = self._count_depth(node.right, depth + 1)
    #     return max(left_depth, right_depth)


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
    res = sol.maxDepth(root)
    print(f"T1: {res}")
