from collections import defaultdict

from sortedcontainers import SortedList


class Leaderboard:
    """Design a leaderboard that tracks player scores.

    Intuition:
        We need efficient updates and top-K queries. A sorted container
        allows O(log n) insertions and removals while maintaining order.

    Approach:
        Use a dictionary to map player IDs to scores, and a SortedList to
        maintain scores in sorted order. For addScore, update both structures.
        For top, sum the last K elements of the sorted list. For reset, remove
        the player's score from both structures.

    Complexity:
        Time: O(log n) for addScore/reset, O(K) for top
        Space: O(n)
    """

    def __init__(self) -> None:
        self.scores: dict[int, int] = defaultdict(int)
        self.rank: SortedList = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.rank.add(score)
        else:
            self.rank.remove(self.scores[playerId])
            self.scores[playerId] += score
            self.rank.add(self.scores[playerId])

    def top(self, k: int) -> int:
        return sum(self.rank[-k:])

    def reset(self, playerId: int) -> None:
        self.rank.remove(self.scores.pop(playerId))
