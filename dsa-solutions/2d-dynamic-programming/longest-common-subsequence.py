class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R, C = len(text1), len(text2)
        pr = [0] * (C + 1)
        for i in range(R):
            cr = [0] * (C + 1)
            for j in range(C):
                cr[j + 1] = max(cr[j], pr[j + 1]) if text1[i] != text2[j] else 1 + pr[j]
            pr = cr
        return pr[-1]


# Time Complexity: O(m * n) [m: text1 length, n: text2 length]
# Space Complexity: O(n) [n: text2 length]
