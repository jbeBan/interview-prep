class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = s[l] == s[r] and (r - l < 2 or dp[l + 1][r - 1])
        p, c = [], []

        def dfs(l: int) -> None:
            if l == n:
                p.append(c.copy())
                return
            for r in range(l, n):
                if dp[l][r]:
                    c.append(s[l : r + 1])
                    dfs(r + 1)
                    c.pop()

        dfs(0)
        return p


# Time Complexity: O(n * 2^n)
# Space Complexity: O(n^2)
