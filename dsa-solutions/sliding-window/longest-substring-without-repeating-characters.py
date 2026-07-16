class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u = set()
        ls = 0
        l = 0
        for r in range(len(s)):
            while s[r] in u:
                u.remove(s[l])
                l += 1
            u.add(s[r])
            ls = max(ls, r - l + 1)
        return ls


# Time Complexity: O(n)
# Space Complexity: O(n)
