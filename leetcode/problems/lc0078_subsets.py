from copy import copy
from typing import List


class LC0078_Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        # Ext loop: all nums
        for n in nums:

            newSets = []

            # Int loop #1: add n to existing sets
            for prevSet in res:
                # C#: newSets.Add(new List<int>(prevSet) { n });
                newSets.append(prevSet + [n])

            # Int loop #2: add new sets to res
            for newSet in newSets:
                res.append(newSet)

        return res
