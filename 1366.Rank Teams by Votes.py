from collections import defaultdict


class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        """Rank teams by votes using positional voting.

        Intuition:
            Each position in a vote carries weight. A team ranked first by
            more voters should appear earlier. Ties are broken by subsequent
            positions, then alphabetically.

        Approach:
            Count how many times each team appears at each position. Sort
            teams by their count vector in descending order, breaking ties
            by alphabetical order (ascending).

        Complexity:
            Time: O(v * t + t * t * log t) where v is votes and t is teams.
            Space: O(t^2)
        """
        num_positions = len(votes[0])
        position_counts: dict[str, list[int]] = defaultdict(lambda: [0] * num_positions)

        for vote in votes:
            for position, team in enumerate(vote):
                position_counts[team][position] += 1

        return "".join(
            sorted(
                votes[0],
                key=lambda team: (position_counts[team], -ord(team)),
                reverse=True,
            )
        )
