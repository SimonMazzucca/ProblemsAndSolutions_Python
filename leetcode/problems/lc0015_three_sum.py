from typing import List


class LC0015_Three_Sum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        i = 0

        while i < len(nums) and nums[i] <= 0:
            if i == 0 or (nums[i - 1] != nums[i]):
                self.__twoSumII(nums, i, res)
            i = i + 1

        return res

    def __twoSumII(self, nums, i, res):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[right] + nums[left]

            if sum < 0:
                left = left + 1
            elif sum > 0:
                right = right - 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left = left + 1
                right = right - 1

                while left < right and nums[left] == nums[left - 1]:
                    left = left + 1
