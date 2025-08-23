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
    # NOTE: Time = O(n), Space = O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        t = head
        while t:
            t = head.next
            head.next = prev
            prev = head
            head = t
        return prev

    # NOTE: Time = O(n), Space = O(n)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     n = head
    #     temp = []
    #     while n != None:
    #         temp.append(n.val)
    #         n = n.next
    #
    #     curr = None
    #     new_head = None
    #     for t in temp:
    #         ln = ListNode(t)
    #         if curr != None:
    #             ln.next = curr
    #
    #         new_head = ln
    #         curr = ln
    #
    #     return new_head


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    ll = LinkedList()
    for i in range(8):
        ll.append(i)
    print(ll.to_list())
    r = sol.reverseList(ll.head)
    while r != None:
        print(r.val)
        r = r.next
