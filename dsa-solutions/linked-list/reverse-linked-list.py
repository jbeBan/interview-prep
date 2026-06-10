from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional[ListNode] = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p


# Time Complexity: O(n)
# Space Complexity: O(1)
