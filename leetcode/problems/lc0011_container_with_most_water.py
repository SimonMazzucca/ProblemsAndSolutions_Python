from typing import List


class LC0011_Container_With_Most_Water:
    def maxArea(self, height: List[int]) -> int:

        res = 0

        left_index = 0
        right_index = len(height)-1

        while left_index < right_index:
            left_height = height[left_index]
            right_height = height[right_index]
            min_height = min(left_height, right_height)
            base = right_index - left_index
            area = min_height * base
            res = max(res, area)

            if left_height < right_height:
                left_index = left_index + 1
            else:
                right_index = right_index - 1

        return res
