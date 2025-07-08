class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Count-based approach: Calculate minimum swaps needed to make binary string alternating

        Intuition:
        To make a binary string alternating, we can either start with '0' or '1'.
        We count misplaced characters for both patterns and find the minimum swaps.

        Approach:
        1. Count total zeros and ones in the string
        2. Check if an alternating pattern is possible (difference ≤ 1)
        3. For valid cases, calculate minimum swaps by counting misplaced chars
        4. Return the minimum number of swaps needed (each swap fixes 2 positions)

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(1) as we only use constant extra space
        """
        # Count zeros and ones
        n0 = s.count('0')
        n1 = len(s) - n0

        # Check if alternating pattern is possible
        if abs(n0 - n1) > 1:
            return -1

        def count_misplaced(expected_first: str) -> int:
            count = 0
            for i, char in enumerate(s):
                # Check if character is misplaced
                if i % 2 == 0:
                    if char != expected_first:
                        count += 1
                else:
                    if char == expected_first:
                        count += 1
            return count // 2  # Each swap fixes 2 positions

        # If equal counts, try both patterns and take minimum
        if n0 == n1:
            return min(count_misplaced('0'), count_misplaced('1'))

        # Otherwise, only one pattern is possible based on which count is higher
        return count_misplaced('0' if n0 > n1 else '1')
