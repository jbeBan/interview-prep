import heapq

from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = list(c.values())
        heapq.heapify_max(h)
        q = deque()
        t = 0
        while h or q:
            t += 1
            if not h:
                t = q[0][1]
            else:
                cc = heapq.heappop_max(h) - 1
                if cc:
                    q.append([cc, t + n])
            if q and q[0][1] == t:
                heapq.heappush_max(h, q.popleft()[0])
        return t


# Time Complexity: O(n * m) [m: tasks length]
# Space Complexity: O(1) [26 unique letters]
