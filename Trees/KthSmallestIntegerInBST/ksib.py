from typing import Optional, List

# TODO: There are improvments on space. Morris Travel.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        path = []
        self._inorder(root, path)
        return path[k - 1]

    def _inorder(self, root: Optional[TreeNode], path: List[int]):
        if not root:
            return
        self._inorder(root.left, path)
        path.append(root.val)
        self._inorder(root.right, path)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 1
    tr = TreeNode(2)
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    tr.left = t1
    tr.right = t3
    res = sol.kthSmallest(tr, 1)
    print(f"T1: {res}")

    # ANS: 5
    tr = TreeNode(4)
    t3 = TreeNode(3)
    t5 = TreeNode(5)
    t2 = TreeNode(2)
    tr.left = t3
    tr.right = t5
    t3.left = t2
    res = sol.kthSmallest(tr, 4)
    print(f"T1: {res}")
