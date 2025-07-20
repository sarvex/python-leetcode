from typing import List
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """Optimized approach using index-based overlap calculation

        Intuition: Group indices by their remainder when divided by k, then find the
        maximum length alternating subsequence between pairs of remainder groups.

        Approach:
        1. Group indices of elements by their remainder when divided by k
        2. Calculate the maximum length of a single remainder group
        3. For each pair of remainder groups, calculate the maximum length of alternating subsequence
        4. Return the maximum length found

        Complexity:
        Time: O(n + r²), where n is the length of nums and r is the number of distinct remainders
        Space: O(n) for storing indices grouped by remainder
        """
        # Define a helper function to calculate overlap (as a local function, not a true lambda)
        # True lambdas in Python are limited to single expressions and can't contain statements
        def calculate_overlap(a: List[int], b: List[int]) -> int:
            """Calculate the maximum length of alternating subsequence between two lists."""
            # Start with 1 if a[0] < b[0], otherwise -1
            start = 1 if a[0] < b[0] else -1
            i, j = 0, 0
            n, m = len(a), len(b)
            ans = 0

            # Iterate through both lists to find alternating elements
            while i < n and j < m:
                if start == 1:  # Looking for element from list a
                    if a[i] > b[j]:  # Skip b elements until we find one that comes after a[i]
                        j += 1
                        continue
                    ans += 1
                    i += 1
                    start = -1  # Switch to looking for element from list b
                    continue

                # start == -1, looking for element from list b
                if b[j] > a[i]:  # Skip a elements until we find one that comes after b[j]
                    i += 1
                    continue
                ans += 1
                j += 1
                start = 1  # Switch to looking for element from list a

            # Handle case where we can add one more element from either list
            return ans + 1 if (start == 1 and i < n) or (start == -1 and j < m) else ans
        # Group indices by their remainder when divided by k
        remainder_groups = defaultdict(list)
        for i, num in enumerate(nums):
            remainder_groups[num % k].append(i)

        # Initialize max_length with the size of the largest remainder group
        max_length = max((len(indices) for indices in remainder_groups.values()), default=0)

        # Convert values to list for easier iteration
        remainder_lists = list(remainder_groups.values())
        n = len(remainder_lists)

        # Compare each pair of remainder groups
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate maximum alternating subsequence length
                max_length = max(max_length, calculate_overlap(remainder_lists[i], remainder_lists[j]))

        return max_length
