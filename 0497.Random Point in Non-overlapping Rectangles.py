from bisect import bisect_left
from random import randint
from typing import List


class Solution:
  def __init__(self, rects: List[List[int]]):
    self.rects = rects
    self.s = [0] * len(rects)
    for i, (x1, y1, x2, y2) in enumerate(rects):
      self.s[i] = self.s[i - 1] + (x2 - x1 + 1) * (y2 - y1 + 1)

  def pick(self) -> List[int]:
    v = randint(1, self.s[-1])
    idx = bisect_left(self.s, v)
    x1, y1, x2, y2 = self.rects[idx]
    return [randint(x1, x2), randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
