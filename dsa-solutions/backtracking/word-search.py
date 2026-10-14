class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if min(r, c) < 0 or r >= R or c >= C or board[r][c] != word[i] or (r, c) in v:
                return False
            b = False
            v.add((r, c))
            for dr, dc in D:
                b |= dfs(r + dr, c + dc, i + 1)
            v.remove((r, c))
            return b

        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False


# Time Complexity: O(m * 4^n) [m: board size, n: word length]
# Space Complexity: O(m) [m: board size]
