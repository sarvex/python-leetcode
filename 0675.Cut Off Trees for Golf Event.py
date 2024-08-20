from heapq import heappop, heappush
from typing import List


class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    def distance(i, j, x, y):
      return abs(i - x) + abs(j - y)

    def search(i, j, x, y):
      q = [(distance(i, j, x, y), i, j)]
      dist = {i * n + j: 0}
      while q:
        _, i, j = heappop(q)
        step = dist[i * n + j]
        if (i, j) == (x, y):
          return step
        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
          c, d = i + a, j + b
          if 0 <= c < m and 0 <= d < n and forest[c][d] > 0:
            if c * n + d not in dist or dist[c * n + d] > step + 1:
              dist[c * n + d] = step + 1
              heappush(q, (dist[c * n + d] + distance(c, d, x, y), c, d))
      return -1

    m, n = len(forest), len(forest[0])
    trees = [
      (forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1
    ]
    trees.sort()
    i = j = 0
    ans = 0
    for _, x, y in trees:
      t = search(i, j, x, y)
      if t == -1:
        return -1
      ans += t
      i, j = x, y
    return ans
