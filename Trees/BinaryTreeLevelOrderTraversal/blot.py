from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n), Space = O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []
        while q:
            ql = len(q)
            level = []
            for _ in range(ql):
                curr = q.pop(0)
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level:
                res.append(level)

        return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    tr = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    tr.left = t2
    tr.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    res = sol.levelOrder(tr)
    print(f"T1: {res}")

    tr = TreeNode(1)
    res = sol.levelOrder(tr)
    print(f"T2: {res}")

    res = sol.levelOrder(None)
    print(f"T3: {res}")

    tr = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    tr.left = t2
    t2.left = t3
    t3.left = t4
    t4.left = t5
    res = sol.levelOrder(tr)
    print(f"T1: {res}")
