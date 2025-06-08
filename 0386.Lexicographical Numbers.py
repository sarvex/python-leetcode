from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """Generate numbers from 1 to n in lexicographical order.

        Intuition:
        Lexicographical order is essentially dictionary order, where numbers are
        treated as strings. We can simulate this by traversing the number space
        in a specific pattern - first going deeper (multiplying by 10) when possible,
        then incrementing and backtracking when necessary.

        Approach:
        1. Start with number 1
        2. For each step:
           a. Add current number to result
           b. If current number * 10 <= n, go one level deeper (v *= 10)
           c. Otherwise, increment current number by 1
           d. If we reach a number ending with 9 or exceed n, backtrack by dividing by 10
              and then increment

        Complexity:
        Time: O(n) - We generate exactly n numbers with constant work per number
        Space: O(n) - For storing the result array
        """
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            # Try to go one level deeper (e.g., 1 -> 10)
            if current * 10 <= n:
                current *= 10
            else:
                # If we can't go deeper, increment and handle edge cases
                # If current ends with 9 or current+1 > n, we need to backtrack
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                    if current == 0:  # Edge case: we've backtracked all the way
                        return result
                current += 1

        return result
