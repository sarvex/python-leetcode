class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """Check if a number is a power of three using iterative division.
        
        Intuition:
        A number is a power of three if we can repeatedly divide it by 3
        until we reach 1. If at any point the division is not exact, 
        the number is not a power of three.
        
        Approach:
        Use iterative division by 3. Continue dividing while n > 1.
        If n becomes indivisible by 3 before reaching 1, return False.
        Handle edge cases: n <= 0 returns False, n == 1 returns True.
        
        Complexity:
        Time: O(log₃(n)) - we divide by 3 at most log₃(n) times
        Space: O(1) - only using constant extra space
        """
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
            
        return n == 1
