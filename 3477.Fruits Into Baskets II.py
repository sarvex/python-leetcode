from typing import List


class Solution:
    """Calculate the number of fruits that cannot be placed in baskets due to capacity constraints.

    Intuition:
        For each fruit, we need to find a basket with sufficient capacity to hold it.
        We use a greedy approach to place each fruit in the first available basket
        that can accommodate it.

    Approach:
        1. Initialize a tracking array to mark which baskets have been used
        2. For each fruit, iterate through baskets to find the first available one
           with sufficient capacity
        3. Mark the basket as used and decrement the unplaced count
        4. Return the final count of unplaced fruits

    Complexity:
        Time: O(m * n) where m is the number of baskets and n is the number of fruits
        Space: O(m) for the basket tracking array
    """
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Total number of fruits initially unplaced
        unplaced_count: int = len(fruits)

        # Track which baskets have been used (indexed by basket position)
        used_baskets: List[bool] = [False] * len(baskets)

        # Try to place each fruit in an available basket
        for fruit_size in fruits:
            # Look for the first available basket that can hold this fruit
            for basket_index, basket_capacity in enumerate(baskets):
                # If basket has sufficient capacity and is available
                if basket_capacity >= fruit_size and not used_baskets[basket_index]:
                    # Mark basket as used and decrement unplaced count
                    used_baskets[basket_index] = True
                    unplaced_count -= 1
                    # Move to next fruit (important: break inner loop, not outer)
                    break

        return unplaced_count
