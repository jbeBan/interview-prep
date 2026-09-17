class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = m = t = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            m = max(m, counts[s[r]])
            while (r - l + 1) - m > k:
                counts[s[l]] -= 1
                l += 1
            t = max(t, r - l + 1)
        return t


# Time Complexity: O(n)
# Space Complexity: O(m) [m: string unique characters]
