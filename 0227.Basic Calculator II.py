class Solution:
    def calculate(self, s: str) -> int:
        """Stack-based evaluation with operator precedence for +-*/.

        Intuition:
            Process each number with the preceding operator. Addition and
            subtraction push to the stack; multiplication and division modify
            the top of the stack immediately.

        Approach:
            1. Iterate through characters, accumulating digits into a number.
            2. When an operator or end of string is reached, apply the previous
               operator to the accumulated number.
            3. Sum all values on the stack for the final result.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        current_value, length = 0, len(s)
        prev_sign = "+"
        stack: list[int] = []
        for idx, char in enumerate(s):
            if char.isdigit():
                current_value = current_value * 10 + int(char)
            if idx == length - 1 or char in "+-*/":
                match prev_sign:
                    case "+":
                        stack.append(current_value)
                    case "-":
                        stack.append(-current_value)
                    case "*":
                        stack.append(stack.pop() * current_value)
                    case "/":
                        stack.append(int(stack.pop() / current_value))
                prev_sign = char
                current_value = 0
        return sum(stack)
