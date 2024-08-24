from functools import lru_cache
from math import inf
from typing import List


class Solution:
  def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
    @lru_cache(None)
    def search(l: int, r: int, k: int) -> List[int]:
      if l == r:
        return [1, 1]
      if l > r:
        return search(r, l, k)

      a = inf
      b = -inf

      # Enumerate all possible positions
      for i in range(1, l + 1):
        for j in range(l - i + 1, r - i + 1):
          if not l + r - k // 2 <= i + j <= (k + 1) // 2:
            continue
          x, y = search(i, j, (k + 1) // 2)
          a = min(a, x + 1)
          b = max(b, y + 1)

      return [a, b]

    return search(firstPlayer, n - secondPlayer + 1, n)
