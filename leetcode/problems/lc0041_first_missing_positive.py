from typing import List


class LC0041_First_Missing_Positive:

    def firstMissingPositive(self, nums: List[int]) -> int:

        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        vals = set(nums)
        res = 1

        while res in vals:
            res = res + 1

        return res
