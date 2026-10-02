class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l: int, r: int) -> tuple[int, int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - (l + 1), l + 1, r

        m = l = r = 0
        for i in range(len(s)):
            pm, pl, pr = palindrome(i, i)
            if pm > m:
                m, l, r = pm, pl, pr
            pm, pl, pr = palindrome(i, i + 1)
            if pm > m:
                m, l, r = pm, pl, pr
        return s[l:r]


# Time Complexity: O(n^2)
# Space Complexity: O(1)
