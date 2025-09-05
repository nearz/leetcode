from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[int | None]) -> Optional[TreeNode]:
    if not values:
        return None

    if values[0] is None:
        return None

    root = TreeNode(values[0])
    q = [root]
    i = 1

    while q and i < len(values):
        node = q.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root
