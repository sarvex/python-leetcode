from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """Greedy grouping of consecutive cards using a counter.

        Intuition:
            Always start a group from the smallest available card and try to
            form a consecutive sequence of groupSize.

        Approach:
            1. Count card frequencies.
            2. For each card in sorted order, if it's still available, try
               to form a group starting from it.
            3. If any card in the group is missing, return False.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        card_count = Counter(hand)
        for value in sorted(hand):
            if card_count[value]:
                for card in range(value, value + groupSize):
                    if card_count[card] == 0:
                        return False
                    card_count[card] -= 1
                    if card_count[card] == 0:
                        del card_count[card]
        return True
