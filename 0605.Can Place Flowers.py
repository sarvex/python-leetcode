from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Greedy approach with padding to handle edge cases.

        Intuition:
        If a plot is empty and its adjacent plots are also empty, we can plant a flower there.
        To handle edge cases at the beginning and end of the array, we pad the array with 0s.

        Approach:
        1. Pad the flowerbed array with 0s at both ends to simplify edge case handling
        2. Iterate through the padded array (excluding the padding)
        3. For each position, check if it and its adjacent positions are all empty (0s)
        4. If so, plant a flower (set to 1) and decrement the remaining flowers count
        5. Return true if we've placed all required flowers or have no more to place

        Complexity:
        Time: O(n) where n is the length of the flowerbed array
        Space: O(n) for the padded array
        """
        # Early return for edge cases
        if n == 0:
            return True

        # Create a padded copy to handle edge cases
        padded = [0] + flowerbed + [0]

        # Iterate through original array positions
        for i in range(1, len(padded) - 1):
            # Check if current position and adjacent positions are empty
            if padded[i - 1] == 0 and padded[i] == 0 and padded[i + 1] == 0:
                # Plant a flower
                padded[i] = 1
                n -= 1

                # Early return if we've planted all flowers
                if n <= 0:
                    return True

        # Return true if all required flowers were planted
        return n <= 0
