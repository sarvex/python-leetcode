from functools import cache
from typing import List


class Solution:
  def maxStudents(self, seats: List[List[str]]) -> int:
    def index(seat: List[str]) -> int:
      mask = 0
      for i, c in enumerate(seat):
        if c == '.':
          mask |= 1 << i
      return mask

    @cache
    def search(seat: int, i: int) -> int:
      ans = 0
      for mask in range(1 << n):
        if (seat | mask) != seat or (mask & (mask << 1)):
          continue
        cnt = mask.bit_count()
        if i == len(ss) - 1:
          ans = max(ans, cnt)
        else:
          nxt = ss[i + 1]
          nxt &= ~(mask << 1)
          nxt &= ~(mask >> 1)
          ans = max(ans, cnt + search(nxt, i + 1))
      return ans

    n = len(seats[0])
    ss = [index(s) for s in seats]
    return search(ss[0], 0)
