from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """Simulate reveal process in reverse to determine deck order.

        Intuition:
            Reverse the reveal process: start with the largest card and
            simulate placing cards back by rotating the bottom card to top
            before inserting each new card at the front.

        Approach:
            1. Sort deck in descending order.
            2. For each card (largest to smallest), rotate bottom to top of deque,
               then prepend current card.
            3. The resulting deque is the desired deck arrangement.

        Complexity:
            Time: O(n log n) — sorting dominates
            Space: O(n) — deque storage
        """
        queue = deque()
        for value in sorted(deck, reverse=True):
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(value)
        return list(queue)
