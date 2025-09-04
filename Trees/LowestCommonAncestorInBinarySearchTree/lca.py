from typing import List, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # NOTE: Way Cleaner
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or not p or not q:
            return None
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    # NOTE: Time = O(h), Space = O(h), where h is the height of the tree
    # def lowestCommonAncestor(
    #     self, root: TreeNode, p: TreeNode, q: TreeNode
    # ) -> TreeNode:
    #     new_root = self._rooted(root, p, q)
    #     p_path = set()
    #     q_path = set()
    #     self._path(new_root, p, p_path)
    #     self._path(new_root, q, q_path)
    #     inter = p_path & q_path
    #     return inter.pop()
    #
    # def _rooted(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     while root:
    #         if p.val < root.val and q.val < root.val:
    #             root = root.left
    #         elif p.val > root.val and q.val > root.val:
    #             root = root.right
    #         else:
    #             return root
    #
    # def _path(self, root: TreeNode, node: TreeNode, path: Set[TreeNode]):
    #     if not root:
    #         return
    #     if root.val == node.val:
    #         path.add(root)
    #         return
    #
    #     path.add(root)
    #     if node.val < root.val:
    #         self._path(root.left, node, path)
    #     else:
    #         self._path(root.right, node, path)


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 5
    tr = TreeNode(5)
    t3 = TreeNode(3)
    t8 = TreeNode(8)
    t1 = TreeNode(1)
    t4 = TreeNode(4)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t2 = TreeNode(2)
    tr.left = t3
    tr.right = t8
    t3.left = t1
    t3.right = t4
    t1.right = t2
    t8.left = t7
    t8.right = t9
    res = sol.lowestCommonAncestor(tr, t3, t8)
    print(f"T1: {res.val}")

    # ANS: 3
    tr = TreeNode(5)
    t3 = TreeNode(3)
    t8 = TreeNode(8)
    t1 = TreeNode(1)
    t4 = TreeNode(4)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t2 = TreeNode(2)
    tr.left = t3
    tr.right = t8
    t3.left = t1
    t3.right = t4
    t1.right = t2
    t8.left = t7
    t8.right = t9
    res = sol.lowestCommonAncestor(tr, t3, t4)
    print(f"T2: {res.val}")

    # ANS: 3
    tr = TreeNode(3)
    t4 = TreeNode(4)
    res = sol.lowestCommonAncestor(tr, tr, t4)
    print(f"T3: {res.val}")

    # ANS: 5
    tr = TreeNode(5)
    t3 = TreeNode(3)
    t8 = TreeNode(8)
    t1 = TreeNode(1)
    t4 = TreeNode(4)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t2 = TreeNode(2)
    tr.left = t3
    tr.right = t8
    t3.left = t1
    t3.right = t4
    t1.right = t2
    t8.left = t7
    t8.right = t9
    res = sol.lowestCommonAncestor(tr, t2, t9)
    print(f"T4: {res.val}")
