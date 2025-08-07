from typing import List


class Solution:
    """A solution to find the maximum number of fruits that can be collected.

    Intuition:
        The problem involves collecting fruits from a 2D grid with specific movement constraints.
        We can collect fruits along the main diagonal directly, then use dynamic programming
        to calculate optimal paths from the rightmost column and bottom row.

    Approach:
        1. Collect all fruits on the main diagonal (i, i) as these are always reachable
        2. Use dynamic programming from the rightmost column moving leftward
        3. Use dynamic programming from the bottom row moving upward
        4. Track reachable positions and update based on movement constraints
        5. Combine results for the final answer

    Complexity:
        - Time complexity: O(n^2) where n is the grid dimension
        - Space complexity: O(n) for the DP arrays
    """

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        """Calculate the maximum number of fruits that can be collected.

        Args:
            fruits: A 2D grid representing fruit counts at each position

        Returns:
            The maximum number of fruits that can be collected
        """
        grid_size = len(fruits)

        # Collect fruits on the main diagonal (always reachable)
        diagonal_fruits = sum(fruits[i][i] for i in range(grid_size))

        # Initialize DP arrays for bottom and right edges
        # dp_bottom tracks maximum fruits when moving upward from bottom row
        # dp_right tracks maximum fruits when moving leftward from right column
        dp_bottom = [fruits[grid_size-1][0], 0, 0]
        dp_right = [fruits[0][grid_size-1], 0, 0]

        # Track maximum reachable positions
        max_reachable = 2

        # Process each column/row using dynamic programming
        for step in range(1, grid_size-1):
            # Create new DP arrays for this step
            new_dp_bottom = [0] * (max_reachable + 2)
            new_dp_right = [0] * (max_reachable + 2)

            # Update DP values based on previous step and current fruits
            for position in range(max_reachable):
                # For bottom DP: consider moves from previous positions
                prev_max_bottom = max(
                    dp_bottom[position-1],
                    dp_bottom[position],
                    dp_bottom[position+1]
                )
                new_dp_bottom[position] = prev_max_bottom + fruits[grid_size-1-position][step]

                # For right DP: consider moves from previous positions
                prev_max_right = max(
                    dp_right[position-1],
                    dp_right[position],
                    dp_right[position+1]
                )
                new_dp_right[position] = prev_max_right + fruits[step][grid_size-1-position]

            # Update DP arrays for next iteration
            dp_bottom = new_dp_bottom
            dp_right = new_dp_right

            # Update reachability based on movement constraints
            constraint_value = max_reachable - grid_size + 4 + step
            if constraint_value <= 1:
                max_reachable += 1
            elif max_reachable - grid_size + 3 + step > 1:
                max_reachable -= 1

        # Return total fruits: diagonal + right edge + bottom edge
        return diagonal_fruits + dp_right[0] + dp_bottom[0]
