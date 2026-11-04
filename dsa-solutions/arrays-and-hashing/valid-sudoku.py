from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rd = defaultdict(set)
        cd = defaultdict(set)
        sd = defaultdict(set)
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in rd[i] or v in cd[j] or v in sd[(i // 3, j // 3)]:
                    return False
                rd[i].add(v)
                cd[j].add(v)
                sd[(i // 3, j // 3)].add(v)
        return True


# Time Complexity: O(n^2) [n: board length]
# Space Complexity: O(n)
