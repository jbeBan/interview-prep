from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        d = {val: idx for idx, val in enumerate(inorder)}
        self.pi = 0

        def dfs(l, r):
            if l > r:
                return None

            rv = preorder[self.pi]
            self.pi += 1
            rn = TreeNode(rv)
            m = d[rv]
            rn.left = dfs(l, m - 1)
            rn.right = dfs(m + 1, r)
            return rn

        return dfs(0, len(inorder) - 1)


# Time Complexity: O(n)
# Space Complexity: O(n)
