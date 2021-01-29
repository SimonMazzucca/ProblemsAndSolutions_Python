class LC0091_Decode_Ways:
    _memo = None

    def numDecodings(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        # if I don't do this, it will remember the _memo
        # from the previous unit test
        self._memo = {}

        return self.recursiveWithMemo(s, 0)

    def recursiveWithMemo(self, s, index):
        if index == len(s):
            return 1

        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        if index in self._memo:
            return self._memo[index]

        ans = self.recursiveWithMemo(s, index + 1)

        nextTwoDigitNumber = int(s[index: index + 2])
        if nextTwoDigitNumber <= 26:
            ans += self.recursiveWithMemo(s, index + 2)

        self._memo[index] = ans

        return ans
