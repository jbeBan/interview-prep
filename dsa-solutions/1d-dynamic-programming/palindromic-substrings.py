class Solution:
    def countSubstrings(self, s: str) -> int:
        def substring(l: int, r: int) -> int:
            c = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        c = 0
        for i in range(len(s)):
            c += substring(i, i)
            c += substring(i, i + 1)
        return c


# Time Complexity: O(n^2)
# Space Complexity: O(1)
