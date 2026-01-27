from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """Recursive descent parsing with a deque for nested parentheses.

        Intuition:
            Process the expression left to right, using recursion to handle
            parenthesized sub-expressions. A deque allows efficient character
            consumption from the front.

        Approach:
            1. Convert the string to a deque for O(1) popleft
            2. Use recursive DFS: when '(' is encountered, recurse to evaluate
               the sub-expression until ')' is found
            3. Track the current sign and apply +, -, *, / using a stack
            4. Return the sum of the stack as the result

        Complexity:
            Time: O(n) where n is the string length
            Space: O(n) for the deque and recursion stack
        """

        def dfs(queue: deque) -> int:
            num, sign, stack = 0, "+", []
            while queue:
                char = queue.popleft()
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == "(":
                    num = dfs(queue)
                if char in "+-*/)" or not queue:
                    match sign:
                        case "+":
                            stack.append(num)
                        case "-":
                            stack.append(-num)
                        case "*":
                            stack.append(stack.pop() * num)
                        case "/":
                            stack.append(int(stack.pop() / num))
                    num, sign = 0, char
                if char == ")":
                    break
            return sum(stack)

        return dfs(deque(s))
