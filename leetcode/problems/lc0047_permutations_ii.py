from copy import copy
from typing import List


class LC0047_Permutations_II:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []

        if len(nums) == 1:
            # Add just number (not list)
            res.append(nums)

        else:
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])

                    # 1) Remove one item at the time --> partial list
                    pList = copy(nums)
                    del pList[i]

                    # 2) Get its partial result
                    partialListOfLists = self.permuteUnique(pList)

                    # 3) Build full result by
                    #    - adding back i item removed to all lists returned
                    #    - adding such list to result
                    for lst in partialListOfLists:
                        # newP is declared with type hint
                        newP: lst[int] = [nums[i]]
                        newP.extend(lst)
                        res.append(newP)

        return res
