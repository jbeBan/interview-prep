from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        RL, CL = len(grid), len(grid[0])
        v = set()

        def bfs(i: int, j: int) -> int:
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            v.add((i, j))
            a = 1
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for rd, cd in d:
                    nr, nc = r + rd, c + cd
                    if min(nr, nc) < 0 or nr == RL or nc == CL:
                        continue
                    if grid[nr][nc] == 1 and (nr, nc) not in v:
                        q.append((nr, nc))
                        v.add((nr, nc))
                        a += 1
            return a

        m = 0
        for i in range(RL):
            for j in range(CL):
                if grid[i][j] == 1 and (i, j) not in v:
                    a = bfs(i, j)
                    m = max(m, a)
        return m


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
