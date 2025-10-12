class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        Calculate maximum total damage using optimized dynamic programming with sliding window.

        Intuition:
        We can use a sliding window approach with three variables to track the maximum damage.
        The key insight is that for each unique power, we can either take it (and skip the next two) or skip it.

        Approach:
        1. Count occurrences of each power and sort unique powers
        2. Use three variables to track max damage for positions i-3, i-2, i-1
        3. For each power, calculate the maximum damage considering the constraints

        Time Complexity: O(n log n) for sorting, O(n) for the main loop
        Space Complexity: O(n) for storing unique powers and their counts
        """
        from collections import Counter

        # Count occurrences of each power and get sorted unique powers
        points = Counter(power)
        point_keys = sorted(points.keys())

        n = len(point_keys)
        if n == 0:
            return 0

        # Base cases
        three_back = 0
        two_back = point_keys[0] * points[point_keys[0]]

        if n == 1:
            return two_back

        # Handle second element
        one_back = max(two_back, point_keys[1] * points[point_keys[1]])
        if point_keys[1] - point_keys[0] >= 3:
            one_back = two_back + point_keys[1] * points[point_keys[1]]

        # Process remaining elements
        for i in range(2, n):
            current_val = point_keys[i] * points[point_keys[i]]

            if point_keys[i] - point_keys[i - 1] > 2:
                # Can take both current and previous
                new_val = one_back + current_val
            elif i > 1 and point_keys[i] - point_keys[i - 2] > 2:
                # Can take current and two_back, but not previous
                new_val = max(one_back, two_back + current_val)
            else:
                # Can only take current with three_back
                new_val = max(one_back, three_back + current_val)

            # Update the three variables
            three_back, two_back, one_back = two_back, one_back, new_val

        return one_back
