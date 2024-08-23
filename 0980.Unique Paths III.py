from itertools import pairwise
from typing import List


class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    def search(i: int, j: int, k: int) -> int:
      if grid[i][j] == 2:
        return int(k == cnt + 1)
      ans = 0
      for a, b in pairwise(dirs):
        x, y = i + a, j + b
        if 0 <= x < m and 0 <= y < n and (x, y) not in vis and grid[x][y] != -1:
          vis.add((x, y))
          ans += search(x, y, k + 1)
          vis.remove((x, y))
      return ans

    m, n = len(grid), len(grid[0])
    start = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == 1)
    dirs = (-1, 0, 1, 0, -1)
    cnt = sum(row.count(0) for row in grid)
    vis = {start}
    return search(*start, 0)
