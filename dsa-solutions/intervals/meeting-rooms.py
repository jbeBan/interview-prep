from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        si = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if si[i].start < si[i - 1].end:
                return False
        return True


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
