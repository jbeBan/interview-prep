import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            z = x - y if x > y else y - x
            heapq.heappush_max(stones, z)
        return 0 if not stones else stones[0]


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
