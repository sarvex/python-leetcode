from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """Find the maximum length of a valid subsequence.

        Dynamic programming with modular arithmetic

        Intuition:
        We need to find the longest subsequence where each element has a specific
        modular relationship with others. By tracking the state using a 2D array,
        we can efficiently compute the maximum length.

        Approach:
        1. Initialize a 2D array f[k][k] to track subsequence lengths
        2. For each number in nums, compute its modulo k value
        3. For each possible remainder j, find the complementary remainder y
        4. Update the state f[x][y] based on previous state f[y][x]
        5. Keep track of the maximum length found

        Complexity:
        Time: O(n*k²) where n is the length of nums and k is the modulo value (2 in this case)
        Space: O(k²) for the state array
        """
        k = 2  # Modulo value
        # Initialize 2D array to track subsequence lengths
        f = [[0] * k for _ in range(k)]
        max_length = 0

        for num in nums:
            # Get the remainder when divided by k
            remainder = num % k

            for j in range(k):
                # Find complementary remainder
                complement = (j - remainder + k) % k
                # Update the state based on previous state
                f[remainder][complement] = f[complement][remainder] + 1
                # Update maximum length found so far
                max_length = max(max_length, f[remainder][complement])

        return max_length
