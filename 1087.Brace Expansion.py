class Solution:
    def expand(self, s: str) -> list[str]:
        """Generate all words from a brace expansion string in sorted order.

        Intuition:
            Parse brace groups into option lists, then generate all combinations
            via backtracking.

        Approach:
            Parse the string into groups of character options (braces yield
            multiple choices, plain text yields single choices). Use DFS to
            enumerate all combinations and sort the result.

        Complexity:
            Time: O(k^n * n) where k = max options per group, n = groups
            Space: O(k^n * n) for storing all results
        """

        def parse(text: str) -> None:
            if not text:
                return
            if text[0] == "{":
                closing = text.find("}")
                groups.append(text[1:closing].split(","))
                parse(text[closing + 1 :])
            else:
                opening = text.find("{")
                if opening != -1:
                    groups.append(text[:opening].split(","))
                    parse(text[opening:])
                else:
                    groups.append(text.split(","))

        def dfs(depth: int, path: list[str]) -> None:
            if depth == len(groups):
                result.append("".join(path))
                return
            for char in groups[depth]:
                path.append(char)
                dfs(depth + 1, path)
                path.pop()

        groups: list[list[str]] = []
        parse(s)
        result: list[str] = []
        dfs(0, [])
        result.sort()
        return result
