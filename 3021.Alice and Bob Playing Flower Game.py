class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculate the number of valid (x,y) pairs where Alice wins the flower game.

        Tagline: Count valid pairs using odd/even distribution analysis

        Intuition:
        Alice wins when the sum of flowers (x+y) is odd. This happens when one
        coordinate is even and the other is odd. We count all such combinations.

        Approach:
        1. Count odd and even numbers in range [1, n] for x-coordinate
        2. Count odd and even numbers in range [1, m] for y-coordinate
        3. Valid pairs = (odd_x * even_y) + (even_x * odd_y)

        Complexity:
        - Time complexity: O(1) - Simple arithmetic operations
        - Space complexity: O(1) - Only using constant extra space

        Args:
            n: Maximum number of flowers in x-direction (inclusive range [1, n])
            m: Maximum number of flowers in y-direction (inclusive range [1, m])

        Returns:
            Number of valid (x,y) pairs where Alice wins

        Examples:
            >>> Solution().flowerGame(3, 2)
            3
            >>> Solution().flowerGame(1, 1)
            1
        """
        # Count odd and even numbers in x-range [1, n]
        odd_x_count = (n + 1) // 2
        even_x_count = n // 2

        # Count odd and even numbers in y-range [1, m]
        odd_y_count = (m + 1) // 2
        even_y_count = m // 2

        # Alice wins when sum is odd: one coordinate odd, other even
        # Valid pairs: (odd_x, even_y) + (even_x, odd_y)
        return odd_x_count * even_y_count + even_x_count * odd_y_count
