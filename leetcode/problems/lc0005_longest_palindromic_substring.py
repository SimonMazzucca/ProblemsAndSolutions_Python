class LC0005_Longest_Palindromic_Substring:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_start = 0
        max_end = 0

        for i in range(len(s)):

            # try odd
            temp = self.expandFromCenter(s, i, i)
            if temp[2] > max_end - max_start:
                max_start = temp[0]
                max_end = temp[1]

            # try even
            temp = self.expandFromCenter(s, i, i + 1)
            if temp[2] > max_end - max_start:
                max_start = temp[0]
                max_end = temp[1]

        return s[max_start:max_end+1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        left = left + 1
        right = right - 1

        return [left, right, right - left + 1]

