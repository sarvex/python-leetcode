import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """Stack-Based Evaluation.

        Intuition:
            Reverse Polish Notation naturally maps to a stack-based evaluation
            where operands are pushed and operators pop two values to compute.

        Approach:
            Iterate through tokens. Push numbers onto the stack. When an
            operator is encountered, pop two operands, apply the operation,
            and push the result back. Use integer truncation for division.

        Complexity:
            Time: O(n) where n is the number of tokens
            Space: O(n) for the stack
        """
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack: list[int] = []
        for token in tokens:
            if token in operations:
                stack.append(int(operations[token](stack.pop(-2), stack.pop(-1))))
            else:
                stack.append(int(token))
        return stack[0]
