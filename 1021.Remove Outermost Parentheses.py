class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """Remove Outermost Parentheses using depth counting.

        Intuition:
            Track the nesting depth. The outermost parentheses are exactly
            those where depth transitions from 0->1 (open) or 1->0 (close).

        Approach:
            Iterate through each character, maintaining a depth counter. For
            open parens, increment depth and include if depth > 1. For close
            parens, decrement depth and include if depth > 0 after decrement.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        result: list[str] = []
        depth = 0
        for char in s:
            if char == "(":
                depth += 1
                if depth > 1:
                    result.append(char)
            else:
                depth -= 1
                if depth > 0:
                    result.append(char)
        return "".join(result)
