class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pr = [1] * n
        for i in range(m - 2, -1, -1):
            cr = [0] * n
            cr[-1] = 1
            for j in range(n - 2, -1, -1):
                cr[j] = cr[j + 1] + pr[j]
            pr = cr
        return pr[0]


# Time Complexity: O(m * n)
# Space Complexity: O(n)
