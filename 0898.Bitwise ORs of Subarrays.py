from typing import List

class Solution:
    """Highly optimized solution for finding the number of unique bitwise ORs of all non-empty subarrays.

    Approach: Optimized Dynamic Programming with List Tracking
    Intuition: This approach uses a single list to track all possible OR values, avoiding set operations
    and leveraging the convergence property of bitwise OR operations. For each new element, we only
    add new OR values that differ from the previous ones, reducing redundant computations.

    Complexity:
        Time: O(n * k) where n is array length and k is bounded by 32 (number of bits)
        Space: O(k) for storing the OR values
    """
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # List to store all unique OR values computed so far
        or_values = []

        # Index to track the start of the previous iteration's values
        prev_start = 0

        # Process each element in the array
        for num in arr:
            # Current length of or_values before processing this number
            current_length = len(or_values)

            # Add the element itself as a new subarray
            or_values.append(num)

            # For each OR value from the previous iteration, compute new ORs
            # We only process values from prev_start to current_length
            for j in range(prev_start, current_length):
                # Compute OR with current number
                new_or = or_values[j] | num

                # Only add if it's different from the last added value
                # This avoids duplicates and leverages convergence property
                if or_values[-1] != new_or:
                    or_values.append(new_or)

            # Update prev_start for next iteration
            prev_start = current_length

        # Return count of unique OR values
        return len(set(or_values))
