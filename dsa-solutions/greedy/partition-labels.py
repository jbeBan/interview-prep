class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        r = []
        l = e = 0
        for i, c in enumerate(s):
            l += 1
            e = max(e, d[c])
            if i == e:
                r.append(l)
                l = 0
        return r


# Time Complexity: O(n)
# Space Complexity: O(1) [s is lowercase English letters]
