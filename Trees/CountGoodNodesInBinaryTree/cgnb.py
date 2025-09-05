from typing import List, Optional
import os
import importlib.util

# TODO: Implement. How can I clear the path of unneccesary comparison nodes?

file_path = os.path.join("..", "build_tree.py")
spec = importlib.util.spec_from_file_location("bt", file_path)
bt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bt)


class Solution:
    def goodNodes(self, root: bt.TreeNode) -> int:
        pass


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    # ANS: 3
    tr = bt.build_tree([2, 1, 1, 3, None, 1, 5])
    res = sol.goodNodes(tr)
    print(f"T1: {res}")

    # ANS: 4
    # tr = build_tree([1, 2, -1, 3, 4])
    # res = sol.goodNodes(tr)
    # print(f"T2: {res}")

    # ANS: 4
    # tr = build_tree([2, None, 4, 10, 8, None, None, 4])
    # res = sol.goodNodes(tr)
    # print(f"T3: {res}")

    # ANS: 4
    # tr = build_tree(
    #     [
    #         -1,
    #         5,
    #         -2,
    #         4,
    #         4,
    #         2,
    #         -2,
    #         None,
    #         None,
    #         -4,
    #         None,
    #         -2,
    #         3,
    #         None,
    #         -2,
    #         0,
    #         None,
    #         -1,
    #         None,
    #         -3,
    #         None,
    #         -4,
    #         -3,
    #         3,
    #         None,
    #         None,
    #         None,
    #         None,
    #         None,
    #         None,
    #         None,
    #         3,
    #         -3,
    #     ]
    # )
    # res = sol.goodNodes(tr)
    # print(f"T3: {res}")
