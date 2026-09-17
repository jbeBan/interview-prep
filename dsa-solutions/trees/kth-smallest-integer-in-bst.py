from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        c = root
        while c or s:
            while c:
                s.append(c)
                c = c.left
            c = s.pop()
            k -= 1
            if k == 0:
                return c.val
            c = c.right


# Time Complexity: O(h + k) [h: tree height]
# Space Complexity: O(h) [h: tree height]
