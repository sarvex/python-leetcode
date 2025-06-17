class Solution:
    def maxDiff(self, num: int) -> int:
        """Digit replacement strategy to maximize difference.

        Intuition:
        To maximize the difference, we need to make one number as large as possible
        and the other as small as possible while following the rules of digit replacement.

        Approach:
        1. For the maximum value (a): Replace the first non-9 digit with 9
        2. For the minimum value (b):
           - If the first digit is not 1, replace it with 1
           - Otherwise, replace the first digit (after the first position) that is not 0 or 1 with 0

        Complexity:
        Time: O(d) where d is the number of digits in num
        Space: O(d) for storing the string representations

        Args:
            num: The integer to modify

        Returns:
            The maximum possible difference between two integers
        """
        # Convert to string for digit manipulation
        max_val, min_val = str(num), str(num)

        # Create maximum value by replacing first non-9 digit with 9
        for digit in max_val:
            if digit != "9":
                max_val = max_val.replace(digit, "9")
                break

        # Create minimum value
        if min_val[0] != "1":
            # Replace first digit with 1 if it's not already 1
            min_val = min_val.replace(min_val[0], "1")
        else:
            # Find first digit after position 0 that is not 0 or 1
            for digit in min_val[1:]:
                if digit not in "01":
                    min_val = min_val.replace(digit, "0")
                    break

        # Calculate and return the difference
        return int(max_val) - int(min_val)
