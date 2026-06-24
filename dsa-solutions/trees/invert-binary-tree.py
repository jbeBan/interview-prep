from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root]) if root else deque()
        while queue:
            curr = queue.pop()
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
            curr.left, curr.right = curr.right, curr.left
        return root


# Time Complexity: O(n)
# Space Complexity: O(n)
