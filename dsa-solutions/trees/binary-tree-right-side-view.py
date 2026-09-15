from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rs = []
        q = deque([root]) if root else deque([])
        while q:
            l = len(q)
            for i in range(l):
                n = q.pop()
                if i == l - 1:
                    rs.append(n.val)
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
        return rs


# Time Complexity: O(n)
# Space Complexity: O(n)
