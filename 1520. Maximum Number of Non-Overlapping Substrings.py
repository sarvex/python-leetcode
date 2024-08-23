from collections import defaultdict
from typing import List


class Solution:
  def maxNumOfSubstrings(self, s: str) -> List[str]:
    ranges = defaultdict(list)
    for idx, ch in enumerate(s):
      ranges[ch].append(idx)
    for r in ranges:
      left, right = ranges[r][0], ranges[r][-1]+1
      templ, tempr = left, right
      while True:
        for ch in set(s[templ:tempr]):
          templ = min(templ, ranges[ch][0])
          tempr = max(tempr, ranges[ch][-1]+1)
        if (templ, tempr) == (left, right): break
        left, right = templ, tempr
      ranges[r] = (templ, tempr)
    # 3
    sorted_ranges = sorted(ranges.values(), key=lambda pair: pair[1])
    ans, prev = [], 0
    for start, end in sorted_ranges:
      if start >= prev:
        ans.append(s[start:end])
        prev = end
    return ans
