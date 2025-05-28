class Solution:
    def myAtoi(self, s: str) -> int:
        """
        String to Integer (atoi) - Iterative parsing with boundary checks
        
        Intuition:
        Parse a string to extract a valid integer following specific rules:
        1. Skip leading whitespace
        2. Check for optional sign (+ or -)
        3. Read digits until non-digit character or end of string
        4. Handle integer overflow/underflow
        
        Approach:
        1. Skip all leading whitespace characters
        2. Check for a sign character (+ or -) and adjust accordingly
        3. Read and convert consecutive digits to an integer
        4. Check for overflow/underflow at each step
        5. Return the final integer with the correct sign
        
        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(1) as we only use constant extra space
        """
        if not s:
            return 0
            
        # Define integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        INT_DIV_10 = INT_MAX // 10
        
        # Initialize variables
        i = 0
        n = len(s)
        result = 0
        sign = 1
        
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # Check if string only contains whitespace
        if i == n:
            return 0
            
        # Check for sign
        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1
            
        # Process digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow/underflow
            if (result > INT_DIV_10 or 
                (result == INT_DIV_10 and digit > 7)):
                return INT_MAX if sign == 1 else INT_MIN
                
            # Update result
            result = result * 10 + digit
            i += 1
            
        return sign * result
