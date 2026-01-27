class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """Bit-shift scoring based on nesting depth of parentheses.

        Intuition:
        Each "()" contributes 2^depth to the total score. We only need to
        track the current depth and add the contribution when we close a
        pair that was just opened.

        Approach:
        1. Track nesting depth as we scan the string
        2. Increment depth on '(', decrement on ')'
        3. When ')' follows '(', add 2^depth (using bit shift)

        Complexity:
        Time: O(n) where n is the string length
        Space: O(1)
        """
        score = 0
        depth = 0
        for index, char in enumerate(s):
            if char == "(":
                depth += 1
            else:
                depth -= 1
                if s[index - 1] == "(":
                    score += 1 << depth
        return score
