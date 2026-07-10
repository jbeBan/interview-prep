from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = 0

        def dbt(root: Optional[TreeNode]) -> int:
            nonlocal md
            if not root:
                return 0
            hl = dbt(root.left)
            hr = dbt(root.right)
            md = max(md, hl + hr)
            return 1 + max(hl, hr)

        dbt(root)
        return md


# Time Complexity: O(n)
# Space Complexity: O(h) [h: root height]
