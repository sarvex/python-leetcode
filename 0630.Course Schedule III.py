from heapq import heappush, heappop
from typing import List


class Solution:
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    pq = []
    s = 0
    for duration, last in courses:
      heappush(pq, -duration)
      s += duration
      while s > last:
        s += heappop(pq)
    return len(pq)
