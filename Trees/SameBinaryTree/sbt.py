from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Cleaner
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # NOTE: Time = O(n), Space = O(n)
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     if p and not q:
    #         return False
    #     if not p and q:
    #         return False
    #     if p.val != q.val:
    #         return False
    #
    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    pr.left = p2
    pr.right = p3
    qr = TreeNode(1)
    q2 = TreeNode(2)
    q3 = TreeNode(3)
    qr.left = q2
    qr.right = q3
    res = sol.isSameTree(pr, qr)
    print(f"T1: {res}")

    pr = TreeNode(4)
    p2 = TreeNode(7)
    pr.left = p2
    qr = TreeNode(4)
    q2 = TreeNode(7)
    qr.right = q2
    res = sol.isSameTree(pr, qr)
    print(f"T2: {res}")

    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    pr.left = p2
    pr.right = p3
    qr = TreeNode(1)
    q2 = TreeNode(2)
    q3 = TreeNode(3)
    qr.left = q3
    qr.right = q2
    res = sol.isSameTree(pr, qr)
    print(f"T3: {res}")
