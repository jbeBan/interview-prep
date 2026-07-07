from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if self.nodes_differ(p, q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def nodes_differ(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and q) or (p and not q)


# Time Complexity: O(n)
# Space Complexity: O(h) [h: height of p/q]
