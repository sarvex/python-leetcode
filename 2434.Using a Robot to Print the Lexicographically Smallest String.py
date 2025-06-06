from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        """Stack-based greedy approach for lexicographically smallest string.

        Intuition:
        Use a stack to simulate the t operations and track the minimum character
        in the remaining unprocessed string to make optimal decisions at each step.

        Approach:
        1. Count frequency of each character in the string
        2. Initialize a minimum character pointer to 'a'
        3. For each character in s:
           - Decrement its count in the frequency map
           - Update the minimum remaining character
           - Add current character to stack
           - Pop characters from stack that are <= minimum remaining character

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) for the stack and result list
        """
        # Count frequency of each character
        counter = Counter(s)
        result = []
        stack = []
        min_char = 'a'  # Initialize to smallest possible character

        # Process each character in the input string
        for c in s:
            # Update frequency count
            counter[c] -= 1

            # Add current character to stack
            stack.append(c)

            # Update minimum remaining character
            while min_char <= 'z' and counter[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from stack while beneficial
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        # No need to empty the stack separately as we've already handled all characters

        return ''.join(result)
