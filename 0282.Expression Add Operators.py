from typing import List


class Solution:
  def addOperators(self, num: str, target: int) -> List[str]:
    ans = []

    def search(u, prev, curr, path):
      if u == len(num):
        if curr == target:
          ans.append(path)
        return
      for i in range(u, len(num)):
        if i != u and num[u] == '0':
          break
        next = int(num[u: i + 1])
        if u == 0:
          search(i + 1, next, next, path + str(next))
        else:
          search(i + 1, next, curr + next, path + "+" + str(next))
          search(i + 1, -next, curr - next, path + "-" + str(next))
          search(
            i + 1,
            prev * next,
            curr - prev + prev * next,
            path + "*" + str(next),
          )

    search(0, 0, 0, "")
    return ans
