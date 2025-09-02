from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._print(root)
        self._walk(root)
        print("-" * 10)
        self._print(root)
        return root

    def _walk(self, node: Optional[TreeNode]):
        if not node:
            return

        self._walk(node.right)
        self._walk(node.left)
        temp = node.left
        node.left = node.right
        node.right = temp

    def _print(self, node: Optional[TreeNode]):
        if not node:
            return

        print(node.val)
        self._print(node.left)
        self._print(node.right)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()
    root = TreeNode(3)
    two = TreeNode(2)
    three = TreeNode(1)
    root.left = two
    root.right = three

    res = sol.invertTree(root)
    print(f"T1 {res.val}")
