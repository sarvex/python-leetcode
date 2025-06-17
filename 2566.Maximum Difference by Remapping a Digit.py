class Solution:
    def minMaxDifference(self, num: int) -> int:
        """Maximum Difference by Remapping a Digit
        Tagline: Greedy approach with digit remapping

        Intuition:
        To maximize the difference, we need to make one number as large as possible
        and the other as small as possible. For the maximum value, we should replace
        the first non-9 digit with 9. For the minimum value, we should replace the
        first digit with 0.

        Approach:
        1. Convert the number to a string for easier digit manipulation
        2. For the minimum value, replace the first digit with '0'
        3. For the maximum value, find the first digit that isn't '9' and replace
           all occurrences of it with '9'
        4. If all digits are '9', the maximum value is the original number
        5. Return the difference between the maximum and minimum values

        Complexity:
        Time: O(n) where n is the number of digits in the input number
        Space: O(n) for storing the string representation of the number
        """
        s = str(num)

        # Find minimum value by replacing first digit with '0'
        min_val = int(s.replace(s[0], '0'))

        # Find maximum value by replacing first non-9 digit with '9'
        non_nine = next((c for c in s if c != '9'), None)
        if non_nine is not None:
            return int(s.replace(non_nine, '9')) - min_val

        # If all digits are '9', the maximum is the original number
        return num - min_val
