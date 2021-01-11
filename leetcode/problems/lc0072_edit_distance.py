class LC0072_Edit_Distance:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        if len1*len2 == 0:
            return len1+len2

        matrix = [0] * (len1 + 1)
        for y in range(0, len1+1):
            matrix[y] = [0] * (len2 + 1)

        for y in range(1, len1 + 1):
            matrix[y][0] = y
        for x in range(1, len2 + 1):
            matrix[0][x] = x

        for y in range(1, len1 + 1):
            for x in range(1, len2 + 1):
                match = word1[y-1] == word2[x-1]

                prevRow = matrix[y-1][x]
                prevCol = matrix[y][x-1]
                prevColAndRow = matrix[y-1][x-1]-1 if match else matrix[y-1][x-1]

                matrix[y][x] = 1 + min(prevColAndRow, min(prevRow, prevCol))

        return matrix[len1][len2]


