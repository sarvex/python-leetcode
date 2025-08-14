class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """Find the largest 3-digit substring with all same digits.
        
        Intuition:
        We need to find consecutive triplets of the same digit and return the largest one.
        Since we want the largest, we can iterate from 9 down to 0.
        
        Approach:
        1. Iterate through digits 9 to 0 (largest to smallest)
        2. For each digit, create a 3-character string of that digit
        3. Check if this substring exists in the input string
        4. Return the first match found (which will be the largest)
        5. If no match found, return empty string
        
        Complexity:
        Time: O(n) where n is length of num string
        Space: O(1) constant extra space
        
        Args:
            num: String of digits
            
        Returns:
            Largest 3-same-digit substring or empty string if none exists
        """
        for digit in range(9, -1, -1):
            target_substring = str(digit) * 3
            if target_substring in num:
                return target_substring
        return ""
