class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        si = sorted(intervals)
        r = [si[0]]
        for s, e in si:
            pe = r[-1][1]
            if s <= pe:
                r[-1][1] = max(pe, e)
            else:
                r.append([s, e])
        return r


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
