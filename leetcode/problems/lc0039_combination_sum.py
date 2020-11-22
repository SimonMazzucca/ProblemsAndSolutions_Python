from copy import copy
from typing import List


class LC0039_Combination_Sum:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        self.traverseWithDfs(res, combo, candidates, target, 0)
        return res

    def traverseWithDfs(self, res, combo, candidates, remain, nextStart):

        if remain == 0:
            res.append(copy(combo))
            return

        if remain < 0:
            return

        for i in range(nextStart, len(candidates)):
            combo.append(candidates[i])
            self.traverseWithDfs(res, combo, candidates, remain - candidates[i], i)
            del combo[-1]
