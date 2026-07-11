from dataclasses import dataclass
from typing import Optional


class ListNode:
    val: int = 0
    next: ListNode = None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast = head
        for _ in range(n):
            fast = fast.next
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


# Time Complexity: O(l) [l: linked list length]
# Space Complexity: O(1)
