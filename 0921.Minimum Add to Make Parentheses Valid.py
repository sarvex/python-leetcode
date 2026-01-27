class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """Stack-based matching of parentheses to count unmatched ones.

        Intuition:
            Use a stack to match opening and closing parentheses. Any
            unmatched parentheses remaining in the stack represent the
            minimum additions needed.

        Approach:
            1. Iterate through the string.
            2. If current char is ')' and top of stack is '(', pop (matched pair).
            3. Otherwise, push the character onto the stack.
            4. Return the stack size as the number of additions needed.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        stack: list[str] = []
        for char in s:
            if char == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
