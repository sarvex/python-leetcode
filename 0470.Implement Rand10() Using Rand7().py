class Solution:
    def rand10(self) -> int:
        """Rejection sampling from rand7 to generate uniform rand10.

        Intuition:
            Two calls to rand7 generate a uniform value in [1, 49]. By
            rejecting values above 40, the remaining values map uniformly
            to [1, 10].

        Approach:
            Generate a number in [1, 49] using (rand7()-1)*7 + rand7().
            If it is at most 40, return value mod 10 + 1. Otherwise retry.

        Complexity:
            Time: O(1) expected — probability of acceptance is 40/49
            Space: O(1)
        """
        while True:
            row = rand7() - 1
            col = rand7()
            value = row * 7 + col
            if value <= 40:
                return value % 10 + 1
