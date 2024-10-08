from math import sqrt, atan2, acos
from typing import List


class Solution:
  def numPoints(self, darts: List[List[int]], r: int) -> int:
    ans = 1
    for x, y in darts:
      angles = []
      for x1, y1 in darts:
        if (x1 != x or y1 != y) and (d := sqrt((x1 - x) ** 2 + (y1 - y) ** 2)) <= 2 * r:
          angle = atan2(y1 - y, x1 - x)
          delta = acos(d / (2 * r))
          angles.append((angle - delta, +1))  # entry
          angles.append((angle + delta, -1))  # exit
      angles.sort(key=lambda x: (x[0], -x[1]))
      val = 1
      for _, entry in angles:
        ans = max(ans, val := val + entry)
    return ans
