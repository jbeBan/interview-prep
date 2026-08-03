from dataclasses import dataclass
from typing import Optional


class ListNode:
    val: int = 0
    next: ListNode = None


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        c = 0
        s = d = ListNode()
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            t = v1 + v2 + c
            c = t // 10
            s.next = ListNode(val=t % 10)
            s = s.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return d.next


# Time Complexity: O(max(m, n)) [m: l1 length, n: l2 length]
# Space Complexity: O(1)
