from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        k = len(s1)
        t, w = Counter(s1), Counter(s2[:k])
        if w == t:
            return True
        for i in range(k, len(s2)):
            w[s2[i]] += 1
            l = s2[i - k]
            w[l] -= 1
            if not w[l]:
                del w[l]
            if w == t:
                return True
        return False


# Time Complexity: O(n) [n: s2 length]
# Space Complexity: O(1) [26 lowercase English letters]
