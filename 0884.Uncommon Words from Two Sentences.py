from collections import Counter
from typing import List


class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    cnt = Counter(s1.split()) + Counter(s2.split())
    return [s for s, v in cnt.items() if v == 1]
