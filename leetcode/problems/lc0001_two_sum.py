from typing import List


class LC0001_Two_Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            n2 = target - nums[i]
            if n2 in indices and indices[n2] != i:
                return [i, indices[n2]]

        return []
