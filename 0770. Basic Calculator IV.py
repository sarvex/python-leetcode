from functools import cmp_to_key


class Expr:
    def __init__(self) -> None:
        self.coef: int = 0
        self.vars: list[str] = []

    def get_val(self) -> str:
        if not self.coef:
            return ""
        if not self.vars:
            return str(self.coef)
        return str(self.coef) + "*" + "*".join(self.vars)


def multiply(expr1: Expr, expr2: Expr) -> Expr:
    result = Expr()
    result.coef = expr1.coef * expr2.coef
    if result.coef == 0:
        return result
    result.vars = list(sorted(expr1.vars + expr2.vars))
    return result


def merge_expr(stack: list, signs: list, expr: Expr) -> None:
    sign = signs[-1][-1]
    match sign:
        case "+":
            stack[-1].append([expr])
        case "-":
            expr.coef = -expr.coef
            stack[-1].append([expr])
        case "*":
            last = stack[-1][-1]
            merged = []
            for prev in last:
                merged.append(multiply(prev, expr))
            stack[-1][-1] = merged
    signs[-1].pop()


def merge_group(stack: list, signs: list, group: list[Expr]) -> None:
    sign = signs[-1][-1]
    match sign:
        case "+":
            stack[-1].append(group)
        case "-":
            negated = []
            for expr in group:
                expr.coef = -expr.coef
                negated.append(expr)
            stack[-1].append(negated)
        case "*":
            last = stack[-1].pop()
            product = []
            for expr1 in last:
                for expr2 in group:
                    product.append(multiply(expr1, expr2))
            stack[-1].append(product)
    signs[-1].pop()


def compare(first: str, second: str) -> int:
    parts_a, parts_b = first.split("*"), second.split("*")
    if len(parts_a) != len(parts_b):
        return len(parts_b) - len(parts_a)
    return 1 if parts_a > parts_b else -1


def get_sum(current_level: list) -> list[Expr]:
    expr_map: dict[str, int | Expr] = {"": 0}
    for groups in current_level:
        for expr in groups:
            if not expr.vars:
                expr_map[""] += expr.coef
            else:
                key = "*".join(expr.vars)
                if key not in expr_map:
                    expr_map[key] = expr
                else:
                    expr_map[key].coef += expr.coef
    result = [
        expr_map[key]
        for key in sorted(expr_map.keys(), key=cmp_to_key(compare))
        if key != "" and expr_map[key].coef
    ]

    if expr_map[""] != 0:
        constant = Expr()
        constant.coef = expr_map[""]
        result.append(constant)
    return result


def calculate(expression: str, eval_vars: list[str], eval_ints: list[int]) -> list[str]:
    stack: list[list] = [[]]
    signs: list[list[str]] = [["+"]]
    index, length = 0, len(expression)
    var_values = {var: val for var, val in zip(eval_vars, eval_ints)}
    while index < length:
        if expression[index] == " ":
            index += 1
            continue
        if expression[index].isalpha():
            expr = Expr()
            token = expression[index]
            while index + 1 < length and expression[index + 1].isalpha():
                token += expression[index + 1]
                index += 1
            if token in var_values:
                expr.coef = var_values[token]
            else:
                expr.coef = 1
                expr.vars = [token]
            merge_expr(stack, signs, expr)
        elif expression[index].isdigit():
            expr = Expr()
            num = int(expression[index])
            while index + 1 < length and expression[index + 1].isdigit():
                num = num * 10 + int(expression[index + 1])
                index += 1
            expr.coef = num
            merge_expr(stack, signs, expr)
        elif expression[index] in "+-*":
            signs[-1].append(expression[index])
        elif expression[index] == "(":
            stack.append([])
            signs.append(["+"])
        elif expression[index] == ")":
            current_level = get_sum(stack.pop())
            signs.pop()
            merge_group(stack, signs, current_level)
        index += 1
    final = get_sum(stack.pop())
    return [expr.get_val() for expr in final]


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: list[str], evalints: list[int]
    ) -> list[str]:
        """Parse and evaluate symbolic expressions with variable substitution.

        Intuition:
            We need a calculator that handles symbolic algebra, supporting addition,
            subtraction, multiplication of polynomials with variables and constants.

        Approach:
            1. Parse the expression character by character using a stack-based approach
            2. Track operator signs at each nesting level for parentheses
            3. Substitute known variable values during parsing
            4. Merge expression terms by multiplying, adding, or subtracting groups
            5. Collect and simplify like terms, then format the output

        Complexity:
            Time: O(n * 2^v) where n is expression length and v is number of variables
            Space: O(n * 2^v) for storing intermediate expression terms
        """
        return calculate(expression, evalvars, evalints)
