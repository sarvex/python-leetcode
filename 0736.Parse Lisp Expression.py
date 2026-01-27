from collections import defaultdict


class Solution:
    def evaluate(self, expression: str) -> int:
        """Recursive descent parser for Lisp-like expressions.

        Intuition:
            Parse the expression recursively, handling let/add/mult operations.
            Use a scope stack (defaultdict of lists) for variable bindings in
            let expressions, pushing on entry and popping on exit.

        Approach:
            1. Parse integers directly, variables via scope lookup.
            2. For '(' expressions, determine the operator (let/add/mult).
            3. let: bind variables in sequence, evaluate final expression,
               then pop all bindings.
            4. add/mult: evaluate two operands and return their sum/product.

        Complexity:
            Time: O(n) where n is the expression length
            Space: O(n) for recursion and variable scopes
        """

        def parse_variable() -> str:
            nonlocal pos
            start = pos
            while pos < length and expression[pos] not in " )":
                pos += 1
            return expression[start:pos]

        def parse_integer() -> int:
            nonlocal pos
            sign, value = 1, 0
            if expression[pos] == "-":
                sign = -1
                pos += 1
            while pos < length and expression[pos].isdigit():
                value = value * 10 + int(expression[pos])
                pos += 1
            return sign * value

        def evaluate_expr() -> int:
            nonlocal pos
            if expression[pos] != "(":
                return (
                    scope[parse_variable()][-1]
                    if expression[pos].islower()
                    else parse_integer()
                )
            pos += 1
            if expression[pos] == "l":
                pos += 4
                bound_vars: list[str] = []
                while True:
                    var_name = parse_variable()
                    if expression[pos] == ")":
                        result = scope[var_name][-1]
                        break
                    bound_vars.append(var_name)
                    pos += 1
                    scope[var_name].append(evaluate_expr())
                    pos += 1
                    if not expression[pos].islower():
                        result = evaluate_expr()
                        break
                for var_name in bound_vars:
                    scope[var_name].pop()
            else:
                is_add = expression[pos] == "a"
                pos += 4 if is_add else 5
                operand_a = evaluate_expr()
                pos += 1
                operand_b = evaluate_expr()
                result = operand_a + operand_b if is_add else operand_a * operand_b
            pos += 1
            return result

        pos, length = 0, len(expression)
        scope: dict[str, list[int]] = defaultdict(list)
        return evaluate_expr()
