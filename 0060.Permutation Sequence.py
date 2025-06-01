class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """Get the kth permutation sequence of numbers 1 to n.

        Intuition: Use factorial number system to find the kth permutation directly
        without generating all permutations.

        Approach: For each position, calculate which number should be placed based on
        factorial values. Remove the used number from the candidates list and continue
        to the next position with updated k value.

        Complexity:
            Time: O(n²) due to removing elements from the candidates list
            Space: O(n) for storing the result and candidates list
        """
        # Adjust k to 0-indexed for easier calculation
        k -= 1

        # Initialize candidates and result
        candidates = list(range(1, n + 1))
        result = []

        # Calculate factorial of (n-1) for the first position
        factorial = 1
        for i in range(1, n):
            factorial *= i

        # For each position, determine which number to use
        for i in range(n - 1, -1, -1):
            # Find the index of the number to use at this position
            idx = k // factorial if i > 0 else 0

            # Add the corresponding number to the result
            result.append(str(candidates[idx]))

            # Remove the used number from candidates
            candidates.pop(idx)

            # Update k for the next position
            k %= factorial

            # Update factorial for the next position
            factorial = factorial // i if i > 0 else 1

        return ''.join(result)
