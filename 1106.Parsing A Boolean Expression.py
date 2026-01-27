class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """Parse and evaluate a boolean expression using a stack.

        Intuition:
            Boolean expressions nest with operators !, &, |. A stack naturally
            handles the nesting by collecting operands until a closing paren
            triggers evaluation with the most recent operator.

        Approach:
            Push operators and boolean values onto the stack. On encountering
            ')', pop all boolean values, then pop the operator and evaluate.
            Use match/case for operator dispatch. Push the result back.

        Complexity:
            Time: O(n) where n is the length of the expression
            Space: O(n) for the stack
        """
        stack: list[str] = []
        for char in expression:
            if char in "tf!&|":
                stack.append(char)
            elif char == ")":
                true_count = false_count = 0
                while stack[-1] in "tf":
                    true_count += stack[-1] == "t"
                    false_count += stack[-1] == "f"
                    stack.pop()
                match stack.pop():
                    case "!":
                        char = "t" if false_count else "f"
                    case "&":
                        char = "f" if false_count else "t"
                    case "|":
                        char = "t" if true_count else "f"
                stack.append(char)
        return stack[0] == "t"
