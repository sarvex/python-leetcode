class Solution:
    def clumsy(self, n: int) -> int:
        """Compute the clumsy factorial using *, /, +, - in cyclic order.

        Intuition:
            The operations cycle every four numbers: multiply, divide, add,
            subtract. Use a stack to handle operator precedence naturally.

        Approach:
            Push n onto a stack. For each subsequent number, apply the current
            cyclic operation: multiply and floor-divide modify the stack top,
            add pushes positive, subtract pushes negative. Sum the stack.

        Complexity:
            Time: O(n) iterating from n down to 1
            Space: O(n) for the stack
        """
        operation = 0
        stack = [n]
        for value in range(n - 1, 0, -1):
            if operation == 0:
                stack.append(stack.pop() * value)
            elif operation == 1:
                stack.append(int(stack.pop() / value))
            elif operation == 2:
                stack.append(value)
            else:
                stack.append(-value)
            operation = (operation + 1) % 4
        return sum(stack)
