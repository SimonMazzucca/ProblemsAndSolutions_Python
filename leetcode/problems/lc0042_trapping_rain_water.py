from typing import List


class LC0042_Trapping_Rain_Water:
    def trap(self, height: List[int]) -> int:
        temp_max = 0
        res = 0
        max_from_l = [0] * len(height)
        max_from_r = [0] * len(height)

        for i in range(len(height)):
            temp_max = max(temp_max, height[i])
            max_from_l[i] = temp_max

        temp_max = 0

        for i in reversed(range(len(height))):
            temp_max = max(temp_max, height[i])
            max_from_r[i] = temp_max

        for i in reversed(range(len(height))):
            res = res + min(max_from_r[i], max_from_l[i]) - height[i]

        return res
