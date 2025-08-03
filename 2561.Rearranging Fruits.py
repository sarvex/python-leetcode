from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Calculate the minimum cost to make two baskets equal through fruit exchanges.

        Intuition:
        Two baskets are equal if they contain the same fruits with the same frequencies.
        We can exchange fruits between baskets at a cost equal to the minimum of the two fruits.
        Alternatively, we can use the cheapest fruit as an intermediary for exchanges.

        Approach:
        1. Create frequency counters for both baskets
        2. Remove common fruits that already exist in both baskets
        3. Check if all remaining fruits can be balanced (even counts)
        4. Create lists of fruits that need to be moved from each basket
        5. Sort the lists and pair them optimally
        6. For each pair, choose the minimum cost between direct exchange and using the cheapest fruit

        Complexity:
        Time: O(n log n) due to sorting
        Space: O(n) for storing the counters and move lists
        """
        # Create frequency counters for both baskets
        counter1 = Counter(basket1)
        counter2 = Counter(basket2)
        the_smallest = min(basket1 + basket2)

        # Remove common fruits that already exist in both baskets
        for k in counter1:
            if k in counter2:
                to_remove = min(counter1[k], counter2[k])
                counter1[k] -= to_remove
                counter2[k] -= to_remove

        # Check if all remaining fruits can be balanced (even counts)
        for v in list(counter1.values()) + list(counter2.values()):
            if v % 2 == 1:
                return -1

        # Create lists of fruits that need to be moved from each basket
        to_move1 = []
        for k in counter1:
            to_move1.extend([k] * (counter1[k] // 2))

        to_move2 = []
        for k in counter2:
            to_move2.extend([k] * (counter2[k] // 2))

        # Sort the lists and pair them optimally
        to_move1.sort()
        to_move2.sort(reverse=True)

        # For each pair, choose the minimum cost between direct exchange and using the cheapest fruit
        return sum(min(to_move1[i], to_move2[i], the_smallest * 2) for i in range(len(to_move1)))
