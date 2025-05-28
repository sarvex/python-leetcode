class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Determine if an integer is a palindrome using digit reversal.
        
        Intuition:
            A palindrome reads the same forward and backward. Instead of converting
            to a string, we can reverse the digits mathematically and compare.
            
        Approach:
            1. Handle edge cases: negative numbers and numbers ending with 0 (except 0 itself)
               are not palindromes.
            2. Reverse only half of the number to avoid integer overflow.
            3. Compare the original number with the reversed half.
            4. For odd-length numbers, we need to divide the reversed number by 10.
            
        Complexity:
            Time: O(log n) where n is the input number (we process each digit)
            Space: O(1) as we only use constant extra space
        """
        # Edge cases: negative numbers and non-zero numbers ending with 0
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
            
        reversed_half = 0
        # Reverse half of the number
        while reversed_half < x:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # For even-length palindromes: x == reversed_half
        # For odd-length palindromes: x == reversed_half // 10 (middle digit in reversed_half)
        return x == reversed_half or x == reversed_half // 10
