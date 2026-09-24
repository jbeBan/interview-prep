from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        RL, CL = len(board), len(board[0])

        def bfs(i: int, j: int, v: set[tuple[int, int]]) -> None:
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            v.add((i, j))
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == RL or nc == CL:
                        continue
                    if board[nr][nc] == "O" and (nr, nc) not in v:
                        q.append((nr, nc))
                        v.add((nr, nc))

        v = set()
        for i in range(RL):
            for j in range(CL):
                if i not in (0, RL - 1) and j not in (0, CL - 1):
                    continue
                if board[i][j] == "O" and (i, j) not in v:
                    bfs(i, j, v)
        for i in range(1, RL - 1):
            for j in range(1, CL - 1):
                if board[i][j] == "O" and (i, j) not in v:
                    board[i][j] = "X"


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
