from functools import cache
from typing import List


class Solution:
  def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    @cache
    def search(i: int, j: int, k: int) -> int:
      if i >= len(group):
        return 1 if k == minProfit else 0
      ans = search(i + 1, j, k)
      if j + group[i] <= n:
        ans += search(i + 1, j + group[i], min(k + profit[i], minProfit))
      return ans % (10 ** 9 + 7)

    return search(0, 0, 0)
