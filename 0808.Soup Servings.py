class Solution:
    def soupServings(self, n: int) -> float:
        """
        Optimized recursive solution with memoization and mathematical optimization.

        Intuition:
        This is a probability problem that can be solved with dynamic programming.
        We have two soups (A and B) with n ml each, and we perform one of four
        operations with equal probability (0.25) in each turn. We want to find
        the probability that soup A becomes empty first, plus half the probability
        that both become empty at the same time.

        Approach:
        1. Convert the problem to units of 25ml to reduce state space
        2. Use memoization to avoid recomputing states
        3. Apply mathematical optimization: when n > 4800, probability approaches 1
        4. For each state (a_units, b_units), recursively calculate the probability
           based on the four possible operations

        Complexity:
        - Time: O(n^2) where n is the number of 25ml units
        - Space: O(n^2) for memoization cache
        """
        # Mathematical optimization: for large n, probability approaches 1
        if n > 4800:
            return 1.0

        # Convert ml to 25ml units for state space reduction
        units = (n + 24) // 25  # Ceiling division

        from functools import cache

        @cache
        def calculate_probability(soup_a_units: int, soup_b_units: int) -> float:
            """
            Calculate the probability that soup A becomes empty first.

            Args:
                soup_a_units: Remaining units of soup A
                soup_b_units: Remaining units of soup B

            Returns:
                Probability that A becomes empty first + 0.5 * both empty together
            """
            # Base cases
            if soup_a_units <= 0 and soup_b_units <= 0:
                # Both soups empty at same time - count as half a success
                return 0.5
            if soup_a_units <= 0:
                # Soup A empty first - full success
                return 1.0
            if soup_b_units <= 0:
                # Soup B empty first - no success
                return 0.0

            # Four operations with equal probability (0.25)
            operation_1 = calculate_probability(soup_a_units - 4, soup_b_units)      # Serve 100ml A, 0ml B
            operation_2 = calculate_probability(soup_a_units - 3, soup_b_units - 1)  # Serve 75ml A, 25ml B
            operation_3 = calculate_probability(soup_a_units - 2, soup_b_units - 2)  # Serve 50ml A, 50ml B
            operation_4 = calculate_probability(soup_a_units - 1, soup_b_units - 3)  # Serve 25ml A, 75ml B

            return 0.25 * (operation_1 + operation_2 + operation_3 + operation_4)

        return calculate_probability(units, units)
