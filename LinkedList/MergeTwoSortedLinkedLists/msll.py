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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        h = res

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                res.next = list2
                list2 = list2.next
                res = res.next

        if list1:
            res.next = list1
        elif list2:
            res.next = list2

        return h.next


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    l_one = LinkedList()
    l_one.add(1, 2, 4)
    l_two = LinkedList()
    l_two.add(3, 5, 6, 7, 8)
    r = sol.mergeTwoLists(l_one.head, l_two.head)
    while r:
        print(r.val)
        r = r.next
