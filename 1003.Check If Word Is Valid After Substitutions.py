class Solution:
    def isValid(self, s: str) -> bool:
        """Check if a string can be built by repeatedly inserting "abc".

        Intuition:
            Every valid string can be reduced to empty by repeatedly removing
            the substring "abc", similar to matching parentheses with a stack.

        Approach:
            Use a stack. Push each character; whenever the top three characters
            form "abc", pop them. The string is valid if the stack is empty at
            the end.

        Complexity:
            Time: O(n) single pass through the string
            Space: O(n) for the stack
        """
        if len(s) % 3:
            return False
        stack: list[str] = []
        for char in s:
            stack.append(char)
            if "".join(stack[-3:]) == "abc":
                stack[-3:] = []
        return not stack
