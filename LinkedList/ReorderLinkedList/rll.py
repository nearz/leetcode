from collections.abc import Iterable
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        ln = ListNode(val)

        if self.head == None and self.tail == None:
            self.head = ln
            self.tail = ln
        else:
            self.tail.next = ln
            self.tail = ln

        self.length += 1

    def add(self, *args):
        if (
            len(args) == 1
            and isinstance(args[0], Iterable)
            and not isinstance(args[0], (str, bytes))
        ):
            items = args[0]
        else:
            items = args

        for i in items:
            self.append(i)

    def to_list(self) -> List:
        res = []
        if self.head == None and self.tail == None:
            return res
        n = self.head
        while n != None:
            res.append(n.val)
            n = n.next
        return res


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    l = LinkedList()
    l.add(2, 4, 6, 8)
    r = sol.reorderList(l.head)
