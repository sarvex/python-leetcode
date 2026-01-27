class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """Split a string in balanced strings using greedy counting.

        Intuition:
            A balanced string has equal L and R characters. Greedily split
            whenever the running balance reaches zero.

        Approach:
            Track a balance counter: increment for 'L', decrement for 'R'.
            Each time balance hits zero, we found a balanced substring.

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(1)
        """
        result = balance = 0
        for char in s:
            if char == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                result += 1
        return result
