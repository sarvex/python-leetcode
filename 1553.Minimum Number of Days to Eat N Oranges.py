from functools import cache


class Solution:
  def minDays(self, n: int) -> int:
    @cache
    def search(n: int) -> int:
      if n < 2:
        return n
      return 1 + min(n % 2 + search(n // 2), n % 3 + search(n // 3))

    return search(n)
