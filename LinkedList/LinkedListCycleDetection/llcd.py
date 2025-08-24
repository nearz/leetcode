from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # NOTE: After seeing explanation on fast and slow pointer, cleaner than mine
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head

        while f:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False

    # NOTE: Time = O(n), Space = O(1)
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     s = head
    #     f = head
    #     c = 1
    #
    #     while f:
    #         if c % 2 == 0:
    #             s = s.next
    #         f = f.next
    #         c += 1
    #         if s == f:
    #             return True
    #
    #     return False

    # Note: Time = O(n), Space = O(n)
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     n = head
    #     seen = set()
    #     while n:
    #         if n in seen:
    #             return True
    #         seen.add(n)
    #         n = n.next
    #
    #     return False


if __name__ == "__main__":
    print("MAIN:")
    sol = Solution()

    n4 = ListNode(4)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n4.next = n2
    n1 = ListNode(1, n2)
    r = sol.hasCycle(n1)
    print(f"T1: {r}")
