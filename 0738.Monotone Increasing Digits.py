class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """Greedy digit scan to find the largest monotone increasing number ≤ n.

        Intuition:
            Scan left-to-right to find the first position where a digit decreases.
            From that point, decrement the previous digit and set all subsequent
            digits to 9.

        Approach:
            1. Convert n to a list of digit characters.
            2. Walk forward while digits are non-decreasing.
            3. Walk backward from the first decrease, decrementing and adjusting.
            4. Fill the remaining suffix with '9'.

        Complexity:
            Time: O(D) where D is the number of digits
            Space: O(D)
        """
        digits = list(str(n))
        i = 1
        while i < len(digits) and digits[i - 1] <= digits[i]:
            i += 1
        if i < len(digits):
            while i and digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                i -= 1
            i += 1
            while i < len(digits):
                digits[i] = "9"
                i += 1
        return int("".join(digits))
