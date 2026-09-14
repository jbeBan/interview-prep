import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [(math.sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]

# Time Complexity: O(n + klog(n))
# Space Complexity: O(n)
