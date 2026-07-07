from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode = None
    right: TreeNode = None


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        stack = [root] if root else None
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and self.subtree(node, subRoot):
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False

    def subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        if root.val != subRoot.val:
            return False
        return self.subtree(root.left, subRoot.left) and self.subtree(
            root.right, subRoot.right
        )


# Time Complexity: O(n * m) [n: nodes in main tree, m: nodes in subtree]
# Space Complexity: O(h_n + h_m) [h_n: height of main tree, h_n: height of subtree]
