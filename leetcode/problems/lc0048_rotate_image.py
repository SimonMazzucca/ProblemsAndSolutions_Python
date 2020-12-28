from typing import List


class LC0048_Rotate_Image:

    def rotate(self, matrix: List[List[int]], rotations) -> None:
        length = len(matrix)
        rotations = rotations % 4

        half_row = length // 2 + length % 2
        half_col = length // 2

        for r in range(half_row):
            for c in range(half_col):
                to_rotate = [None] * 4
                row = r
                col = c

                for i in range(0, 4):
                    to_rotate[i] = matrix[row][col]
                    orig_row = row
                    row = col
                    col = length - 1 - orig_row

                for i in range(0, 4):
                    matrix[row][col] = to_rotate[(i + 4 - rotations) % 4]
                    orig_row = row
                    row = col
                    col = length - 1 - orig_row
