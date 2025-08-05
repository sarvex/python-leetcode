from collections import defaultdict
from typing import List


class Solution:
    """Optimized sliding window approach using defaultdict for maximum fruit collection.

    Intuition:
        Find the longest contiguous subarray with at most 2 distinct elements using
        an optimized sliding window technique with early deletion for efficiency.

    Approach:
        1. Use start/end pointers to maintain a sliding window
        2. Use defaultdict to track fruit types and counts
        3. Expand window by moving end pointer and adding fruits
        4. When more than 2 fruit types exist, shrink window from start with early deletion
        5. Track maximum window size throughout process

    Complexity:
        Time: O(n) where n is the number of fruits
        Space: O(1) since we store at most 3 fruit types in the defaultdict
    """
    def totalFruit(self, fruits: List[int]) -> int:
        # Start pointer of sliding window
        start: int = 0

        # Track fruit types and their counts in current window
        visited: defaultdict = defaultdict(int)

        # Maximum fruits collected so far
        max_len: int = 0

        # End pointer moves through all fruits
        for end in range(len(fruits)):
            # Add current fruit to window
            visited[fruits[end]] += 1

            # Shrink window while we have 3 or more fruit types
            while len(visited) >= 3:
                # Early deletion optimization: remove fruit completely if count is 1
                if visited[fruits[start]] == 1:
                    del visited[fruits[start]]
                else:
                    visited[fruits[start]] -= 1

                # Move start pointer to shrink window
                start += 1

            # Update maximum fruits with current window size
            max_len = max(max_len, end - start + 1)

        return max_len
