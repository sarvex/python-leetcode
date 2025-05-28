class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert Roman numeral to integer.
        
        Intuition:
        Roman numerals are read from left to right. When a smaller value precedes a larger value,
        it represents subtraction, otherwise it represents addition.
        
        Approach:
        1. Create a mapping of Roman symbols to their integer values.
        2. Iterate through adjacent pairs of characters using pairwise.
        3. For each pair (a, b), if value of a is less than value of b, subtract a's value,
           otherwise add a's value.
        4. Add the value of the last character separately since pairwise doesn't include it.
        
        Complexity:
        Time: O(n) where n is the length of the input string
        Space: O(1) as we use a fixed-size dictionary for mapping
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Handle edge case of single character
        if len(s) == 1:
            return values[s]
            
        from itertools import pairwise
        
        total = 0
        # Process all character pairs
        for current, next_char in pairwise(s):
            # If current value is less than next, subtract it (like IV = -1 + 5 = 4)
            # Otherwise add it (like VI = 5 + 1 = 6)
            if values[current] < values[next_char]:
                total -= values[current]
            else:
                total += values[current]
                
        # Add the last character's value which isn't covered by pairwise
        total += values[s[-1]]
        
        return total
