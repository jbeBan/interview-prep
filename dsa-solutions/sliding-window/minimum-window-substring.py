from collections import Counter, defaultdict
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        wc, tc = defaultdict(int), Counter(t)
        m, n = len(wc), len(tc)
        bl, br = -inf, inf
        l = 0
        for r, c in enumerate(s):
            wc[c] += 1
            if c in tc and wc[c] == tc[c]:
                m += 1
            while m == n:
                if r - l < br - bl:
                    bl, br = l, r
                wc[s[l]] -= 1
                if s[l] in tc and wc[s[l]] < tc[s[l]]:
                    m -= 1
                l += 1
        return "" if br - bl + 1 == inf else s[bl : br + 1]


# Time Complexity: O(m + n) [m: t length, n: s length]
# Space Complexity: O(k) [k: s and t unique characters]
