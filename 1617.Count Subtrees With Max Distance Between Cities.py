from collections import defaultdict
from typing import List


class Solution:
  def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
    def search(u: int, d: int = 0):
      nonlocal mx, nxt, msk
      if mx < d:
        mx, nxt = d, u
      msk ^= 1 << u
      for v in g[u]:
        if msk >> v & 1:
          search(v, d + 1)

    g = defaultdict(list)
    for u, v in edges:
      u, v = u - 1, v - 1
      g[u].append(v)
      g[v].append(u)
    ans = [0] * (n - 1)
    nxt = mx = 0
    for mask in range(1, 1 << n):
      if mask & (mask - 1) == 0:
        continue
      msk, mx = mask, 0
      cur = msk.bit_length() - 1
      search(cur)
      if msk == 0:
        msk, mx = mask, 0
        search(nxt)
        ans[mx - 1] += 1
    return ans
