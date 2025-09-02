from typing import Optional

# TODO: Can be better Time. Seralize and Pattern Matching


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n * m), Space = O(n + h)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        res = []
        while q:
            curr = q.pop(0)
            if curr.val == subRoot.val:
                res.append(self._subComare(curr, subRoot))
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return any(res)

    def _subComare(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self._subComare(p.left, q.left) and self._subComare(p.right, q.right)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: True
    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    pr.left = p2
    pr.right = p3
    p2.left = p4
    p2.right = p5

    qr = TreeNode(2)
    q2 = TreeNode(4)
    q3 = TreeNode(5)
    qr.left = q2
    qr.right = q3

    res = sol.isSubtree(pr, qr)
    print(f"T1: {res}")

    # ANS: False
    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    pr.left = p2
    pr.right = p3
    p2.left = p4
    p2.right = p5
    p4.left = p6

    qr = TreeNode(2)
    q2 = TreeNode(4)
    q3 = TreeNode(5)
    qr.left = q2
    qr.right = q3

    res = sol.isSubtree(pr, qr)
    print(f"T2: {res}")

    # ANS: True
    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p22 = TreeNode(2)
    pr.left = p2
    pr.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p22

    qr = TreeNode(2)
    q2 = TreeNode(4)
    q3 = TreeNode(5)
    qr.left = q2
    qr.right = q3

    res = sol.isSubtree(pr, qr)
    print(f"T3: {res}")

    # ANS: False
    pr = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p22 = TreeNode(2)
    pr.left = p2
    pr.right = p3
    p2.left = p4
    p2.right = p5
    p4.left = p6
    p3.left = p22

    qr = TreeNode(2)
    q2 = TreeNode(4)
    q3 = TreeNode(5)
    qr.left = q2
    qr.right = q3

    res = sol.isSubtree(pr, qr)
    print(f"T4: {res}")
