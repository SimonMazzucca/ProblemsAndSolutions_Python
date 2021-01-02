from typing import List


class LC0054_Spiral_Matrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0

        rows = len(matrix)
        cols = len(matrix[0])
        cells = rows * cols

        r = 0
        c = 0

        ans = []

        while cells > 0:
            ans.append(matrix[r][c])
            matrix[r][c] = 101
            cells = cells - 1

            newR = r + dirs[dir][0]
            newC = c + dirs[dir][1]

            if (0 <= newR < rows) and (0 <= newC < cols) and (matrix[newR][newC] != 101):
                r = newR
                c = newC
            else:
                dir = (dir + 1) % 4
                r += dirs[dir][0]
                c += dirs[dir][1]

        return ans
