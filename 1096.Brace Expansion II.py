class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        """Expand brace expression via recursive substitution.

        Intuition:
            Find the innermost brace pair, expand its comma-separated options,
            and recursively process the resulting expressions until no braces
            remain.

        Approach:
            Locate the first closing brace and the matching opening brace.
            Split the content between them by commas, substitute each option
            into the surrounding string, and recurse. Collect unique results
            in a set and return sorted.

        Complexity:
            Time: O(k * n) where k is the number of generated strings and n is expression length
            Space: O(k) for the result set
        """

        def dfs(exp: str) -> None:
            closing = exp.find("}")
            if closing == -1:
                results.add(exp)
                return
            opening = exp.rfind("{", 0, closing - 1)
            prefix, suffix = exp[:opening], exp[closing + 1 :]
            for middle in exp[opening + 1 : closing].split(","):
                dfs(prefix + middle + suffix)

        results: set[str] = set()
        dfs(expression)
        return sorted(results)
