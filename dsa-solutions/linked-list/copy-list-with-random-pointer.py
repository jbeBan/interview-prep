from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Node = None
    random: Node = None


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        n_map = defaultdict(lambda: Node(-1))
        n_map[None] = None
        curr = head
        while curr:
            n_map[curr].val = curr.val
            n_map[curr].next = n_map[curr.next]
            n_map[curr].random = n_map[curr.random]
            curr = curr.next
        return n_map[head]


# Time Complexity: O(n)
# Space Complexity: O(n)
