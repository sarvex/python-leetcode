class Solution:
    def parseTernary(self, expression: str) -> str:
        """Stack-based right-to-left evaluation of nested ternary expressions.

        Intuition:
            Processing from right to left, values are pushed onto a stack.
            When a '?' is encountered, the next character is the condition
            that determines which of the two stacked values to keep.

        Approach:
            1. Traverse the expression from right to left.
            2. Skip ':' characters.
            3. On '?', set a flag indicating the next character is a condition.
            4. When the condition is read, pop two values and keep the correct one
               based on whether the condition is 'T' or 'F'.
            5. Otherwise, push the character onto the stack.

        Complexity:
            Time: O(n) where n is the length of the expression.
            Space: O(n) for the stack.
        """
        stack: list[str] = []
        is_condition = False
        for char in expression[::-1]:
            if char == ":":
                continue
            if char == "?":
                is_condition = True
            else:
                if is_condition:
                    if char == "T":
                        true_value = stack.pop()
                        stack.pop()
                        stack.append(true_value)
                    else:
                        stack.pop()
                    is_condition = False
                else:
                    stack.append(char)
        return stack[0]
