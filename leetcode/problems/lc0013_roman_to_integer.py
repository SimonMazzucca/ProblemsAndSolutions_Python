class LC0013_Roman_to_Integer:
    def romanToInt(self, s: str) -> int:

        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        prev = 0
        res = 0

        while i < len(s):
            curr = vals[s[i]]
            i = i + 1

            if prev != 0 and curr > prev:
                # remove previous
                res -= prev
                # add correct value
                res += curr - prev
            else:
                res += curr

            prev = curr

        return res
