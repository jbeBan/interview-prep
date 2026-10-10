class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        p = []
        s = []

        def gen_paren(l: int, r: int) -> None:
            if l == r == n:
                p.append("".join(s))
                return
            if l < n:
                s.append("(")
                gen_paren(l + 1, r)
                s.pop()
            if r < l:
                s.append(")")
                gen_paren(l, r + 1)
                s.pop()

        gen_paren(0, 0)
        return p


# Time Complexity: O(4^n / sqrt(n)) [n: parentheses pairs count]
# Space Complexity: O(n) [n: parentheses pairs count]
