class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            t = (n >> i) & 1
            r |= t << (31 - i)
        return r


# Time Complexity: O(1)
# Space Complexity: O(1)
