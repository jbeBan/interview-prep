import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.m_heap = nums.copy()
        heapq.heapify(self.m_heap)
        while len(self.m_heap) > k:
            heapq.heappop(self.m_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.m_heap, val)
        if len(self.m_heap) > self.size:
            heapq.heappop(self.m_heap)
        return self.m_heap[0]


# Time Complexity: O(mlog(k)) [m: number of add() calls]
# Space Complexity: O(k)
