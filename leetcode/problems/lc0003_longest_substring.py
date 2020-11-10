from typing import List


class LC0003_Longest_Substring_Without_Repeating_Characters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        m = 0
        left = 0
        right = 0

        while left < len(s) and right < len(s):
            if s[right] in char_set:
                char_set.remove(s[left])
                left = left + 1
            else:
                char_set.add(s[right])
                right = right + 1

            m = max(m, right - left)

        return m
