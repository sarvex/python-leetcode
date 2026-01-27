class Solution:
    def solveEquation(self, equation: str) -> str:
        """Parse and solve a linear equation by extracting x-coefficients and constants.

        Intuition:
        Split the equation at '=', parse each side to extract the coefficient of x
        and the constant term, then solve for x algebraically.

        Approach:
        1. Define a parser that extracts total x-coefficient and constant from an expression.
        2. Parse both sides of the equation.
        3. If x-coefficients are equal, check constants for infinite or no solution.
        4. Otherwise compute x = (constant_right - constant_left) / (coeff_left - coeff_right).

        Complexity:
        Time: O(n)
        Space: O(1)
        """

        def parse_expression(expr: str) -> tuple[int, int]:
            x_coeff = constant = 0
            if expr[0] != "-":
                expr = "+" + expr
            idx, length = 0, len(expr)
            while idx < length:
                sign = 1 if expr[idx] == "+" else -1
                idx += 1
                end = idx
                while end < length and expr[end] not in "+-":
                    end += 1
                token = expr[idx:end]
                if token[-1] == "x":
                    x_coeff += sign * (int(token[:-1]) if len(token) > 1 else 1)
                else:
                    constant += sign * int(token)
                idx = end
            return x_coeff, constant

        left_expr, right_expr = equation.split("=")
        x_left, const_left = parse_expression(left_expr)
        x_right, const_right = parse_expression(right_expr)
        if x_left == x_right:
            return "Infinite solutions" if const_left == const_right else "No solution"
        return f"x={(const_right - const_left) // (x_left - x_right)}"
