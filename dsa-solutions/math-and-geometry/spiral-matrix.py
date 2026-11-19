class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        s = [len(matrix[0]), len(matrix) - 1]
        l = []
        d, r, c = 0, 0, -1
        while s[d & 1]:
            for _ in range(s[d & 1]):
                r += D[d][0]
                c += D[d][1]
                l.append(matrix[r][c])
            s[d & 1] -= 1
            d = (d + 1) % 4
        return l


# Time Complexity: O(m * n)
# Space Complexity: O(1)
