class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """Stack-based simulation of baseball scoring rules.

        Intuition:
            Each operation modifies a record stack: numbers push scores,
            '+' sums the last two, 'D' doubles the last, 'C' removes the last.

        Approach:
            1. Iterate through operations using a stack to track scores.
            2. Apply each operation rule to modify the stack.
            3. Return the sum of all remaining scores.

        Complexity:
            Time: O(n) where n is the number of operations
            Space: O(n) for the score stack
        """
        stack: list[int] = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] << 1)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
