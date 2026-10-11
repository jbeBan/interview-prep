class Solution:
    def countBits(self, n: int) -> list[int]:
        def count(i: int) -> int:
            c = 0
            for _ in range(32):
                c += i & 1
                i >>= 1
            return c

        c = []
        for i in range(n + 1):
            c.append(count(i))
        return c


# Time Complexity: O(n)
# Space Complexity: O(n)
