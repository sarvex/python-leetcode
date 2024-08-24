from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
  def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    cnt = [0] * n
    g = defaultdict(int)
    for a, b in edges:
      a, b = a - 1, b - 1
      a, b = min(a, b), max(a, b)
      cnt[a] += 1
      cnt[b] += 1
      g[(a, b)] += 1

    s = sorted(cnt)
    ans = [0] * len(queries)
    for i, t in enumerate(queries):
      for j, x in enumerate(s):
        k = bisect_right(s, t - x, lo=j + 1)
        ans[i] += n - k
      for (a, b), v in g.items():
        if cnt[a] + cnt[b] > t >= cnt[a] + cnt[b] - v:
          ans[i] -= 1
    return ans
