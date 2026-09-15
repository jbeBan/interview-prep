from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes(n: TreeNode, m: int) -> int:
            if not n:
                return 0
            gn = 1 if m <= n.val else 0
            cm = max(n.val, m)
            gn += good_nodes(n.left, cm)
            gn += good_nodes(n.right, cm)
            return gn

        return good_nodes(root, root.val)


# Time Complexity: O(n)
# Space Complexity: O(n)
