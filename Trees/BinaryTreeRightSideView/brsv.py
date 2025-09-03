from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Time = O(n), Space = O(w), w max width of a level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
                res.append(level[-1])

        return res


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: [1, 3]
    tr = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    tr.left = t2
    tr.right = t3
    res = sol.rightSideView(tr)
    print(f"T1: {res}")

    # ANS: [1, 2]
    tr = TreeNode(1)
    t2 = TreeNode(2)
    tr.left = t2
    res = sol.rightSideView(tr)
    print(f"T2: {res}")

    # ANS: [1, 3, 7]
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
    res = sol.rightSideView(tr)
    print(f"T3: {res}")

    # ANS: [1, 3, 6]
    tr = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    tr.left = t2
    tr.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    res = sol.rightSideView(tr)
    print(f"T4: {res}")
