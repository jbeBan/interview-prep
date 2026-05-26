class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts: dict[str, int] = {}
        t_counts: dict[str, int] = {}
        for s_char, t_char in zip(s, t):
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
            t_counts[t_char] = t_counts.get(t_char, 0) + 1
        return s_counts == t_counts


# Time Complexity: O(n + m) [n: length of s, m: length of t]
# Space Complexity: O(1) [26 lowercase English letters]
