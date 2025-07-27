class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        """
        Maximize subarrays by removing one conflicting pair optimally.

        Intuition:
        Use sweep line algorithm with greedy interval selection to efficiently
        calculate the maximum gain from removing any single conflicting pair.

        Approach:
        1. Sort pairs by their right endpoint for optimal processing order
        2. Use greedy selection to track the most restrictive constraints
        3. Calculate removal gains by tracking alternative constraint choices
        4. Return total subarrays minus base restrictions plus maximum gain

        Complexity:
        Time: O(k log k) where k = len(conflictingPairs)
        Space: O(1)
        """
        # Adjust n for 1-indexed processing and add sentinel
        n += 1
        conflictingPairs.sort(key=lambda p: max(*p))
        conflictingPairs.append([n, n])

        max_diff = 0      # Maximum gain from removing any pair
        max_left = 0      # Current most restrictive left boundary
        rem = 0           # Current total restrictions
        max_altleft = 0   # Second most restrictive left boundary
        altrem = 0        # Alternative restrictions count

        # Process pairs in order of increasing right endpoint
        for left, right in conflictingPairs:
            # Normalize pair to (left, right)
            if left > right:
                left, right = right, left

            if left > max_left:
                # Found new most restrictive constraint
                # Calculate gain from removing previous most restrictive
                max_diff = max(
                    max_diff,
                    (max_altleft - max_left) * (n - right) + rem - altrem
                )

                # Update alternative tracking
                altrem = rem
                max_altleft = max_left

                # Add restrictions from new constraint
                rem += (left - max_left) * (n - right)
                max_left = left

            elif left > max_altleft:
                # Update second most restrictive constraint
                altrem += (left - max_altleft) * (n - right)
                max_altleft = left

        # Return total subarrays minus base restrictions plus maximum gain
        return (n - 1) * n // 2 - rem + max_diff
