from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        RL, CL = len(grid), len(grid[0])
        n = 0

        def bfs(i: int, j: int) -> None:
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            grid[i][j] = "0"
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == RL or nc == CL or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for i in range(RL):
            for j in range(CL):
                if grid[i][j] == "0":
                    continue
                bfs(i, j)
                n += 1
        return n


# Time complexity: O(m * n)
# Space complexity: O(m * n)
