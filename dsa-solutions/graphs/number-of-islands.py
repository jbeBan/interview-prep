from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        RL, CL = len(grid), len(grid[0])
        v = set()

        def bfs(i: int, j: int) -> None:
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            v.add((i, j))
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == RL or nc == CL:
                        continue
                    if grid[nr][nc] == "1" and (nr, nc) not in v:
                        q.append((nr, nc))
                        v.add((nr, nc))

        n = 0
        for i in range(RL):
            for j in range(CL):
                if grid[i][j] == "1" and (i, j) not in v:
                    bfs(i, j)
                    n += 1
        return n


# Time complexity: O(m * n)
# Space complexity: O(m * n)
