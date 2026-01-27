from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        """Recursive divide-and-conquer with memoization on subexpressions.

        Intuition:
            Each operator splits the expression into left and right parts.
            We recursively compute all possible results for each part and
            combine them.

        Approach:
            Use a cached recursive function that splits the expression at
            every operator. For each split, compute all left and right
            results and combine using the operator. Base case: a pure
            number returns itself.

        Complexity:
            Time: O(n * 2^n) Catalan number of possible trees
            Space: O(n * 2^n) for memoized results
        """

        @cache
        def search(exp: str) -> list[int]:
            if exp.isdigit():
                return [int(exp)]
            results = []
            for i, char in enumerate(exp):
                if char in "-+*":
                    left, right = search(exp[:i]), search(exp[i + 1 :])
                    for left_val in left:
                        for right_val in right:
                            if char == "-":
                                results.append(left_val - right_val)
                            elif char == "+":
                                results.append(left_val + right_val)
                            else:
                                results.append(left_val * right_val)
            return results

        return search(expression)
