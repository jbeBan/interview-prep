class Solution:
    def hammingWeight(self, n: int) -> int:
        m = 0
        for _ in range(32):
            m += n & 1
            n >>= 1
        return m


# Time Complexity: O(1)
# Space Complexity: O(1)
