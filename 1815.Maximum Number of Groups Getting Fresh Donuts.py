from functools import cache
from typing import List


class Solution:
  def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
    @cache
    def search(state, mod):
      res = 0
      x = int(mod == 0)
      for i in range(1, batchSize):
        if state >> (i * 5) & 31:
          t = search(state - (1 << (i * 5)), (mod + i) % batchSize)
          res = max(res, t + x)
      return res

    state = ans = 0
    for v in groups:
      i = v % batchSize
      ans += i == 0
      if i:
        state += 1 << (i * 5)
    ans += search(state, 0)
    return ans
