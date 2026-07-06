from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h = {None: 0}
        stack = [(root, False)] if root else []
        while stack:
            n, v = stack.pop()
            if v:
                if abs(h[n.left] - h[n.right]) > 1:
                    return False
                h[n] = max(h[n.left], h[n.right]) + 1
                continue
            stack.append((n, True))
            if n.right:
                stack.append((n.right, False))
            if n.left:
                stack.append((n.left, False))
        return True


# Time Complexity: O(n)
# Space Complexity: O(n)
