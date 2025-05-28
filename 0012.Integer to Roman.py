class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert integer to Roman numeral.
        
        Greedy approach using symbol mapping and subtraction.
        
        Intuition:
        Roman numerals follow a pattern where larger values are represented first,
        and special cases like 4 (IV) and 9 (IX) use subtraction. A greedy approach
        works well by starting with the largest possible symbols.
        
        Approach:
        1. Create two parallel lists: one with Roman symbols (including compound ones
           like 'CM' for 900) and another with their corresponding values
        2. Iterate through these lists from largest to smallest value
        3. For each value, repeatedly subtract it from the input number and append
           the corresponding symbol until we can't anymore
        4. Continue until the number becomes zero
        
        Complexity:
        Time: O(1) - the algorithm performs a constant number of operations
        Space: O(1) - we only use a fixed amount of extra space
        """
        symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        result = []
        
        for symbol, value in zip(symbols, values):
            while num >= value:
                num -= value
                result.append(symbol)
                
        return ''.join(result)
