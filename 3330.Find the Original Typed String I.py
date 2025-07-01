class Solution:
    def possibleStringCount(self, word: str) -> int:
        """Find the number of possible original strings before typing.

        Tagline: Stack-based approach to count consecutive identical characters

        Intuition:
        When typing, pressing a key twice produces the same character twice in the final string.
        For each group of consecutive identical characters, the number of possible ways to
        type them increases by the length of the group minus 1. This is because each character
        in the group (except the first) could have been produced by either typing it once or
        by pressing the same key twice.

        Approach:
        1. Use a stack to track consecutive identical characters
        2. Start with a base count of 1 (the string itself)
        3. For each character in the word:
           - If stack is empty or current character matches the top of stack, push to stack
           - Otherwise, add (length of stack - 1) to answer and reset stack with current character
        4. After processing all characters, add (length of final stack - 1) to answer
        5. Return the total count

        Complexity:
        Time: O(n) where n is the length of the word
        Space: O(n) in worst case when all characters are identical
        """
        stack = []
        ans = 1

        for char in word:
            if not stack or char == stack[-1]:
                stack.append(char)
            else:
                ans += len(stack) - 1
                stack = [char]

        # Process the final group of characters in the stack
        ans += len(stack) - 1

        return ans
