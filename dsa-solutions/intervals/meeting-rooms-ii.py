import heapq
from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        si = sorted(intervals, key=lambda x: x.start)
        mr = []
        for i in si:
            if mr and mr[0] <= i.start:
                heapq.heappop(mr)
            heapq.heappush(mr, i.end)
        return len(mr)


# TIme Complexity: O(nlog(n))
# Space Complexity: O(n)
