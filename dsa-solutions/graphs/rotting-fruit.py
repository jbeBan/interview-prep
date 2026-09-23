from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        MI, MJ = len(grid), len(grid[0])

        def bfs(q):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            v = set()
            t, r = -1, 0
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if min(ni, nj) < 0 or ni == MI or nj == MJ:
                            continue
                        if grid[ni][nj] == 1 and (ni, nj) not in v:
                            q.append((ni, nj))
                            v.add((ni, nj))
                            r += 1
                t += 1
            return t, r

        f = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    f += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if f == 0:
            return 0
        t, r = bfs(q)
        return t if r == f else -1


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
