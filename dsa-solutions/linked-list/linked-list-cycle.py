from dataclasses import dataclass
from typing import Optional


class ListNode:
    val: int = 0
    next: ListNode = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# Time Complexity: O(n)
# Space Complexity: O(1)
