from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(n: Optional[TreeNode], lm: int, rm: int) -> bool:
            if not n:
                return True
            if not (lm < n.val < rm):
                return False
            return valid(n.left, lm, n.val) and valid(n.right, n.val, rm)

        return valid(root, float("-inf"), float("inf"))


# Time Complexity: O(n)
# Space Complexity: O(h) [h: height of tree]
