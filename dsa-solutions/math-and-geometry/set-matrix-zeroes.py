class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        RL, CL = len(matrix), len(matrix[0])
        rz, cz = [False] * RL, [False] * CL
        for r in range(RL):
            for c in range(CL):
                if not matrix[r][c]:
                    rz[r] = cz[c] = True
        for r in range(RL):
            for c in range(CL):
                if rz[r] or cz[c]:
                    matrix[r][c] = 0


# Time Complexity: O(m * n)
# Space Complexity: O(m + n)
