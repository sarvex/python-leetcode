class Solution:
    def removeStars(self, s: str) -> str:
        """Stack-based character removal for star operations

        Intuition:
            When we see a star, we need to remove the previous character.
            This is a classic stack operation where we push characters and pop when we see a star.

        Approach:
            Use a stack to keep track of characters. For each character in the string:
            - If it's a star ('*'), pop the last character from the stack
            - Otherwise, append the character to the stack
            Finally, join all characters in the stack to form the result string

        Complexity:
            Time: O(n) where n is the length of the input string
            Space: O(n) for storing characters in the stack
        """
        stack = []
        for char in s:
            if char == '*':
                if stack:  # Safety check to prevent popping from empty stack
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
