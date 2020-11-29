from copy import copy
from typing import List


class LC0046_Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        combo = []
        self.recurse(res, combo, nums)
        return res

    def recurse(self, res, combo, nums):
        if len(combo) == len(nums):
            res.append(copy(combo))
            return

        for i in nums:
            if i in combo:
                continue

            combo.append(i)
            self.recurse(res, combo, nums)
            del combo[-1]
