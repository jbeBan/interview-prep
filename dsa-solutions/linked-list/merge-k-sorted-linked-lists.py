import heapq
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: "ListNode | None" = None


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        h = []
        for i, n in enumerate(lists):
            if n:
                heapq.heappush(h, (n.val, i, n))
        r = ListNode()
        c = r
        while h:
            _, i, n = heapq.heappop(h)
            c.next = n
            c = n
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
        return r.next


# Time Complexity: O(nlog(k))
# Space Complexity: O(k)
