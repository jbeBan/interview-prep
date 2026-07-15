import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, u = 1, max(piles)
        k = u
        while l <= u:
            m = (l + u) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / m)
            if t <= h:
                k = m
                u = m - 1
            else:
                l = m + 1
        return k


# Time Complexity: O(nlog(m)) [n: piles length, m: max pile]
# Space Complexity: O(1)
