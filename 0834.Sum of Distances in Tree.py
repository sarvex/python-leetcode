from collections import defaultdict
from typing import List


class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    def search(i: int, fa: int, d: int):
      ans[0] += d
      size[i] = 1
      for j in g[i]:
        if j != fa:
          search(j, i, d + 1)
          size[i] += size[j]

    def find(i: int, fa: int, t: int):
      ans[i] = t
      for j in g[i]:
        if j != fa:
          find(j, i, t - size[j] + n - size[j])

    g = defaultdict(list)
    for a, b in edges:
      g[a].append(b)
      g[b].append(a)

    ans = [0] * n
    size = [0] * n
    search(0, -1, 0)
    find(0, -1, ans[0])
    return ans
