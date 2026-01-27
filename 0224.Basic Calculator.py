class Solution:
    def calculate(self, s: str) -> int:
        """Stack-based evaluation of expressions with parentheses.

        Intuition:
            Use a stack to handle nested parentheses. Track the current result
            and sign, pushing them onto the stack when entering parentheses.

        Approach:
            1. Iterate through the string character by character.
            2. Accumulate digits into a number and add to result with current sign.
            3. On '(', push current result and sign, then reset.
            4. On ')', pop sign and previous result to combine.

        Complexity:
            Time: O(n)
            Space: O(n) for the stack
        """
        stack: list[int] = []
        result, sign = 0, 1
        pos, length = 0, len(s)
        while pos < length:
            if s[pos].isdigit():
                number = 0
                end = pos
                while end < length and s[end].isdigit():
                    number = number * 10 + int(s[end])
                    end += 1
                result += sign * number
                pos = end - 1
            elif s[pos] == "+":
                sign = 1
            elif s[pos] == "-":
                sign = -1
            elif s[pos] == "(":
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif s[pos] == ")":
                result = stack.pop() * result + stack.pop()
            pos += 1
        return result
