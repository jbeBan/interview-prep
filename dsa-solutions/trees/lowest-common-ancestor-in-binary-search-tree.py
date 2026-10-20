from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        c = root
        while c:
            if p.val > c.val and q.val > c.val:
                c = c.right
            elif p.val < c.val and q.val < c.val:
                c = c.left
            else:
                return c


# Time Complexity: O(log(h)) [h: tree height]
# Space Complexity: O(1)
