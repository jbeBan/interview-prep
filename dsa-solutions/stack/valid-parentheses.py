parens = {")": "(", "}": "{", "]": "["}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c not in parens:
                stack.append(c)
                continue
            if not stack or stack.pop() != parens[c]:
                return False
        return not stack


# Time Complexity: O(n)
# Space Complexity: O(n)
