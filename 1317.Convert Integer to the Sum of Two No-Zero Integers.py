from typing import List

class Solution:
    """
    Find two non-zero integers that sum up to n and don't contain any '0' digits.

    Intuition:
    We need to find two positive integers a and b such that a + b = n and neither a nor b
    contains the digit '0'. We can iterate through possible values of a and check if both
    a and (n - a) are non-zero integers.

    Approach:
    1. Iterate through all possible values of a from 1 to n-1
    2. For each a, compute b = n - a
    3. Check if neither a nor b contains the digit '0'
    4. Return the first valid pair [a, b] found

    Complexity:
    - Time: O(n log n), where n is the input number. We check each number up to n,
            and for each number, we check its digits which takes O(log n) time.
    - Space: O(1), we only use a constant amount of extra space.
    """

    def getNoZeroIntegers(self, n: int) -> List[int]:
        """Return a list of two non-zero integers that sum to n."""
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) + str(b):
                return [a, b]
        return []  # Should never reach here per problem constraints
