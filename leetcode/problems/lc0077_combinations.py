from copy import copy
from typing import List


class LC0077_Combinations:

    _ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self._ans = []
        self.backtrack(n, k, 1, [])
        return self._ans

    def backtrack(self, n, k, level, combo):
        if len(combo) == k:
            self._ans.append(copy(combo))
        else:
            for i in range(level, n+1):
                combo.append(i)
                self.backtrack(n, k, i+1, combo)
                combo.pop()



