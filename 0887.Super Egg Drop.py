from functools import cache


class Solution:
  def superEggDrop(self, k: int, n: int) -> int:
    @cache
    def search(i: int, j: int) -> int:
      if i < 1:
        return 0
      if j == 1:
        return i
      l, r = 1, i
      while l < r:
        mid = (l + r + 1) >> 1
        a = search(mid - 1, j - 1)
        b = search(i - mid, j)
        if a <= b:
          l = mid
        else:
          r = mid - 1
      return max(search(l - 1, j - 1), search(i - l, j)) + 1

    return search(n, k)
