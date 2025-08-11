class Solution:
    """Solution for LeetCode 869: Reordered Power of 2."""
    
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Check if digits of n can be reordered to form a power of 2.
        
        Intuition:
        Two numbers can be rearranged to form each other if and only if they have
        the same digit frequency. Instead of generating all permutations of n,
        we can compare digit frequencies with all powers of 2.
        
        Approach:
        1. Generate sorted digit strings for all powers of 2 within integer range
        2. Sort digits of input number n
        3. Check if sorted n matches any sorted power of 2
        
        Complexity:
        Time: O(log n) - sorting digits of n and comparing with precomputed set
        Space: O(1) - constant space for powers of 2 (at most 31 powers)
        
        Args:
            n: Positive integer to check
            
        Returns:
            True if digits can be reordered to form a power of 2, False otherwise
        """
        power_signatures = {''.join(sorted(str(1 << i))) for i in range(31)}
        n_signature = ''.join(sorted(str(n)))
        
        return n_signature in power_signatures