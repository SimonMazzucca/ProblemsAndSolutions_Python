class LC0076_Minimum_Window_Substring:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""

        tCounts = {}
        winCounts = {}

        result = [-1, 0, 0]

        leftPos = 0
        rightPos = 0

        # Alternative way (requires import)
        # tCounts = Counter(t)

        for c in t:
            tCounts[c] = tCounts.get(c, 0) + 1

        required = len(tCounts)

        formed = 0

        # Loop to expand
        while rightPos < len(s):

            c = s[rightPos]
            winCounts[c] = winCounts.get(c, 0) + 1

            if c in tCounts and winCounts[c] == tCounts[c]:
                formed += 1

            # Loop to contract
            while leftPos <= rightPos and formed == required:
                if result[0] == -1 or rightPos - leftPos + 1 < result[0]:
                    result[0] = rightPos - leftPos + 1
                    result[1] = leftPos
                    result[2] = rightPos

                c = s[leftPos]
                winCounts[c] -= 1

                if c in tCounts and winCounts[c] < tCounts[c]:
                    formed -= 1

                leftPos += 1

            rightPos += 1

        if result[0] == -1:
            return ""
        else:
            return s[result[1]:result[2]+1]
