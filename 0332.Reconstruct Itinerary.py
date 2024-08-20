from collections import defaultdict
from typing import List


class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    def search(f: str):
      while g[f]:
        search(g[f].pop())
      ans.append(f)

    g = defaultdict(list)
    for f, t in sorted(tickets, reverse=True):
      g[f].append(t)
    ans = []
    search("JFK")
    return ans[::-1]
