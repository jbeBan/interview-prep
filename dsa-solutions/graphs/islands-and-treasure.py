from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        RL, CL = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(q: list[tuple[int, int]]) -> None:
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            v = set()
            l = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = l
                    for dr, dc in d:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) < 0 or nr == RL or nc == CL:
                            continue
                        if grid[nr][nc] == INF and (nr, nc) not in v:
                            q.append((nr, nc))
                            v.add((nr, nc))
                l += 1
        
        q = deque()
        for r in range(RL):
            for c in range(CL):
                if grid[r][c] == 0:
                    q.append((r, c))
        bfs(q)


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
