from ast import List
from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        q = deque([root]) if root else deque([])
        while q:
            l = []
            for _ in range(len(q)):
                n = q.pop()
                l.append(n.val)
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
            r.append(l)
        return r


# Time Complexity: O(n)
# Space Complexity: O(n)
