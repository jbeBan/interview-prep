class Solution:
    def getSum(self, a: int, b: int) -> int:
        M = 0xFFFFFFFF
        L = 0x7FFFFFFF
        while b:
            c = (a & b) << 1
            a = (a ^ b) & M
            b = c & M
        return a if a <= L else ~(a ^ M)


# Time Complexity: O(1) [32 bits]
# Space Complexity: O(1)
