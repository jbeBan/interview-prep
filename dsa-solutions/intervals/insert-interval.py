class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        r = []
        ns, ne = newInterval
        for i, (s, e) in enumerate(intervals):
            if ne < s:
                r.append([ns, ne])
                return r + intervals[i:]
            if s <= ne and ns <= e:
                ns = min(ns, s)
                ne = max(ne, e)
            else:
                r.append(intervals[i])
        r.append([ns, ne])
        return r


# Time Complexity: O(n)
# Space Complexity: O(n)
