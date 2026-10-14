class Solution:
    def numDecodings(self, s: str) -> int:
        d0, d1, d2 = 0, 1, 0
        for i in range(len(s) - 1, -1, -1):
            d0 += 0 if s[i] == "0" else d1
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                d0 += d2
            d0, d1, d2 = 0, d0, d1
        return d1


# Time Complexity: O(n)
# Space Complexity: O(1)
