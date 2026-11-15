class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        si = sorted(intervals)
        n, pe = 0, si[0][1]
        for i in range(1, len(si)):
            if si[i][0] < pe:
                pe = min(pe, si[i][1])
                n += 1
            else:
                pe = si[i][1]
        return n


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
