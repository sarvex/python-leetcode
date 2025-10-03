from collections import deque
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """Sweep-line over sorted endpoints with cached arrivals.

        Intuition:
        Maintain a running count of active flowers while scanning people times in
        increasing order. Add flowers whose start <= t, and remove flowers whose
        end < t (since end is inclusive), to get the number blooming at t.

        Approach:
        - Sort all starts and ends and keep them as deques for O(1) pops from the left.
        - Iterate people in sorted order; advance pointers and cache the count per t.
        - Map cached counts back to the original people order to form the result.

        Complexity:
        - Time: O(N log N + M log M) for sorting; linear sweep thereafter.
        - Space: O(N + M) for deques and caching.
        """
        if not people:
            return []

        starts = deque(sorted(s for s, _ in flowers))
        ends = deque(sorted(e for _, e in flowers))

        active: int = 0
        counts: dict[int, int] = {}

        for t in sorted(people):
            if t in counts:
                continue
            while starts and starts[0] <= t:
                starts.popleft()  # popleft equivalent but compatible if deques behave
                active += 1
            while ends and ends[0] < t:
                ends.popleft()
                active -= 1
            counts[t] = active

        return [counts[t] for t in people]
