from functools import cache
from math import inf
from typing import List


class Solution:
  def stoneGameIII(self, stoneValue: List[int]) -> str:
    @cache
    def search(i: int) -> int:
      if i >= n:
        return 0
      ans, s = -inf, 0
      for j in range(3):
        if i + j >= n:
          break
        s += stoneValue[i + j]
        ans = max(ans, s - search(i + j + 1))
      return ans

    n = len(stoneValue)
    ans = search(0)
    if ans == 0:
      return 'Tie'
    return 'Alice' if ans > 0 else 'Bob'
