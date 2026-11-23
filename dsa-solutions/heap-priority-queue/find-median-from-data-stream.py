import heapq


class MedianFinder:
    def __init__(self):
        self.l, self.r = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.l, num)
        heapq.heappush(self.r, heapq.heappop_max(self.l))
        if len(self.l) < len(self.r):
            heapq.heappush_max(self.l, heapq.heappop(self.r))

    # Time Complexity: O(log(n))
    # Space Complexity: O(n)

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) / 2

    # Time Complexity: O(1)
    # Space Complexity: O(1)
