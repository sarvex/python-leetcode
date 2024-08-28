from functools import cache


class Solution:
  def possiblyEquals(self, s1: str, s2: str) -> bool:

    def fn(s):
      ans = [int(s)]
      if len(s) == 2:
        if s[1] != '0': ans.append(int(s[0]) + int(s[1]))
        return ans
      elif len(s) == 3:
        if s[1] != '0': ans.append(int(s[:1]) + int(s[1:]))
        if s[2] != '0': ans.append(int(s[:2]) + int(s[2:]))
        if s[1] != '0' and s[2] != '0': ans.append(int(s[0]) + int(s[1]) + int(s[2]))
      return ans

    @cache
    def search(i, j, diff):
      if i == len(s1) and j == len(s2): return diff == 0
      if i < len(s1) and s1[i].isdigit():
        ii = i
        while ii < len(s1) and s1[ii].isdigit(): ii += 1
        for x in fn(s1[i:ii]):
          if search(ii, j, diff - x): return True
      elif j < len(s2) and s2[j].isdigit():
        jj = j
        while jj < len(s2) and s2[jj].isdigit(): jj += 1
        for x in fn(s2[j:jj]):
          if search(i, jj, diff + x): return True
      elif diff == 0:
        if i == len(s1) or j == len(s2) or s1[i] != s2[j]: return False
        return search(i + 1, j + 1, 0)
      elif diff > 0:
        if i == len(s1): return False
        return search(i + 1, j, diff - 1)
      else:
        if j == len(s2): return False
        return search(i, j + 1, diff + 1)

    return search(0, 0, 0)
