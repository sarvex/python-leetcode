from typing import List


class Solution:
  def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    def search(source, target, seen):
      x, y = source
      if (
          not (0 <= x < 10 ** 6 and 0 <= y < 10 ** 6)
          or (x, y) in blocked
          or (x, y) in seen
      ):
        return False
      seen.add((x, y))
      if len(seen) > 20000 or source == target:
        return True
      for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
        next = [x + a, y + b]
        if search(next, target, seen):
          return True
      return False

    blocked = set((x, y) for x, y in blocked)
    return search(source, target, set()) and search(target, source, set())
