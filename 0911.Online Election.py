from bisect import bisect_right
from collections import Counter


class TopVotedCandidate:
    """Binary search on precomputed winners at each time.

    Intuition:
        Precompute the leading candidate at each voting timestamp so that
        queries can be answered efficiently with binary search.

    Approach:
        1. During initialization, iterate through votes tracking the vote
           count for each person and recording the current leader.
        2. For queries, binary search on times to find the latest timestamp
           <= t and return the corresponding winner.

    Complexity:
        Time: O(n) for init, O(log n) per query
        Space: O(n)
    """

    def __init__(self, persons: list[int], times: list[int]):
        vote_count: Counter[int] = Counter()
        self.times = times
        self.winners: list[int] = []
        current_leader = 0
        for person in persons:
            vote_count[person] += 1
            if vote_count[current_leader] <= vote_count[person]:
                current_leader = person
            self.winners.append(current_leader)

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        return self.winners[idx]
