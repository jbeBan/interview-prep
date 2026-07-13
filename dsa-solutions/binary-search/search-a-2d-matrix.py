from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        k, l = 0, len(matrix[0]) - 1
        while i <= j:
            mr = (i + j) // 2
            if target < matrix[mr][k] and target < matrix[mr][l]:
                j = mr - 1
                continue
            if target > matrix[mr][k] and target > matrix[mr][l]:
                i = mr + 1
                continue
            while k <= l:
                mc = (k + l) // 2
                if target < matrix[mr][mc]:
                    l = mc - 1
                elif target > matrix[mr][mc]:
                    k = mc + 1
                else:
                    return True
            return False
        return False


# Time Complexity: O(log(m * n)) [m: matrix rows, n: matrix columns]
# Space Complexity: O(1)
