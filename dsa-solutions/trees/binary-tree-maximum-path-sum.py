from dataclasses import dataclass
from math import inf


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


class Solution:
    def maxPathSum(self, root: "TreeNode | None") -> int:
        m = -inf

        def dfs(n: "TreeNode | None") -> int:
            nonlocal m
            if not n:
                return 0
            v = n.val
            lv = max(0, dfs(n.left))
            rv = max(0, dfs(n.right))
            m = max(m, v + lv + rv)
            return v + max(lv, rv)

        dfs(root)
        return m


# Time Complexity: O(n)
# Space Complexity: O(h) [h: tree height]
