class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        r = [1, 2]
        for _ in range(n - 2):
            r[0], r[1] = r[1], r[0] + r[1]
        return r[1]


# Time Complexity: O(n)
# Space Complexity: O(1)
