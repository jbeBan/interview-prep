class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        RL, CL = len(heights), len(heights[0])

        def dfs(r: int, c: int, v: set[tuple[int, int]], h: int):
            if (r, c) in v or min(r, c) < 0 or r == RL or c == CL or heights[r][c] < h:
                return
            v.add((r, c))
            dfs(r + 1, c, v, heights[r][c])
            dfs(r, c + 1, v, heights[r][c])
            dfs(r - 1, c, v, heights[r][c])
            dfs(r, c - 1, v, heights[r][c])

        p, a = set(), set()
        for r in range(RL):
            dfs(r, 0, p, heights[r][0])
            dfs(r, CL - 1, a, heights[r][CL - 1])
        for c in range(CL):
            dfs(0, c, p, heights[0][c])
            dfs(RL - 1, c, a, heights[RL - 1][c])
        pa = []
        for r in range(RL):
            for c in range(CL):
                if (r, c) in p and (r, c) in a:
                    pa.append([r, c])
        return pa


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
