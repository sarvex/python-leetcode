from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Backtracking with iterative approach
        
        Intuition:
        Each digit on a phone keypad maps to multiple letters. To find all possible
        combinations, we need to consider each letter for each digit and combine them.
        
        Approach:
        1. Create a mapping of digits to their corresponding letters
        2. Start with an empty combination
        3. For each digit, generate new combinations by appending each possible letter
           to existing combinations
        4. Return all possible combinations
        
        Complexity:
        Time: O(4^n) where n is the length of digits (worst case when digits contain 7 or 9)
        Space: O(4^n) for storing all possible combinations
        """
        if not digits:
            return []
            
        # Mapping of digits to letters (0 and 1 don't map to any letters)
        phone_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        # Start with an empty combination
        combinations = [""]
        
        # Process each digit
        for digit in digits:
            # Get the letters corresponding to the current digit
            letters = phone_map[int(digit) - 2]
            
            # Generate new combinations by appending each letter to existing combinations
            combinations = [combo + letter for combo in combinations for letter in letters]
            
        return combinations
