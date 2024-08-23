from functools import cache


class Solution:
  def winnerSquareGame(self, n: int) -> bool:
    @cache
    def search(i: int) -> bool:
      if i == 0:
        return False
      j = 1
      while j * j <= i:
        if not search(i - j * j):
          return True
        j += 1
      return False

    return search(n)
