from functools import cache
from typing import List


class Solution:
  def diffWaysToCompute(self, expression: str) -> List[int]:
    @cache
    def search(exp):
      if exp.isdigit():
        return [int(exp)]
      ans = []
      for i, c in enumerate(exp):
        if c in '-+*':
          left, right = search(exp[:i]), search(exp[i + 1:])
          for a in left:
            for b in right:
              if c == '-':
                ans.append(a - b)
              elif c == '+':
                ans.append(a + b)
              else:
                ans.append(a * b)
      return ans

    return search(expression)
