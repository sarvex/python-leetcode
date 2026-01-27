class Solution:
    def reverseParentheses(self, s: str) -> str:
        """Reverse substrings within each pair of parentheses using a stack.

        Intuition:
            Process characters left to right. When hitting a closing parenthesis,
            pop and reverse everything back to the matching opening parenthesis.

        Approach:
            Use a stack. Push characters and opening parentheses. On closing
            parenthesis, pop characters until the opening parenthesis, reverse
            them, and push back. Join the final stack for the result.

        Complexity:
            Time: O(n^2) in worst case due to repeated reversals
            Space: O(n)
        """
        stack: list[str] = []
        for char in s:
            if char == ")":
                reversed_segment: list[str] = []
                while stack[-1] != "(":
                    reversed_segment.append(stack.pop())
                stack.pop()
                stack.extend(reversed_segment)
            else:
                stack.append(char)
        return "".join(stack)
