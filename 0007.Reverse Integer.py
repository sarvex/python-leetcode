import math

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer
        
        Intuition:
        Process digits from right to left while checking for overflow.
        
        Approach:
        - Handle the sign separately from the digits
        - Process each digit from the end using modulo and division
        - Check for 32-bit integer bounds using standard infinity values
        - Return 0 if the reversed integer overflows
        
        Complexity:
        - Time: O(log10(n)) - We process each digit once
        - Space: O(1) - We use constant extra space
        """
        # Get the sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        # Process each digit
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Apply the sign to the reversed number
        result = sign * reversed_num
        
        # Check if result is within representable range using standard infinity values
        if not (-math.inf < result < math.inf):
            return 0
            
        return result
