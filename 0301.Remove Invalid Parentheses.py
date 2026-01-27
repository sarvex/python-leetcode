class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        """DFS with pruning to remove minimum invalid parentheses.

        Intuition:
            Count the number of unmatched left and right parentheses, then use
            DFS to try removing exactly that many to produce valid strings.

        Approach:
            1. Count unmatched left and right parentheses by scanning the string.
            2. Use DFS to explore removing each unmatched parenthesis.
            3. Prune branches where remaining characters cannot satisfy the removal
               count or where right count exceeds left count.
            4. Collect valid results in a set to avoid duplicates.

        Complexity:
            Time: O(2^n) in the worst case where n is the length of the string
            Space: O(n) for recursion depth and result storage
        """

        def dfs(
            index: int,
            open_remove: int,
            close_remove: int,
            open_count: int,
            close_count: int,
            current: str,
        ) -> None:
            if index == length:
                if open_remove == 0 and close_remove == 0:
                    results.add(current)
                return
            if length - index < open_remove + close_remove or open_count < close_count:
                return
            if s[index] == "(" and open_remove:
                dfs(
                    index + 1,
                    open_remove - 1,
                    close_remove,
                    open_count,
                    close_count,
                    current,
                )
            elif s[index] == ")" and close_remove:
                dfs(
                    index + 1,
                    open_remove,
                    close_remove - 1,
                    open_count,
                    close_count,
                    current,
                )
            dfs(
                index + 1,
                open_remove,
                close_remove,
                open_count + (s[index] == "("),
                close_count + (s[index] == ")"),
                current + s[index],
            )

        open_remove = close_remove = 0
        for char in s:
            if char == "(":
                open_remove += 1
            elif char == ")":
                if open_remove:
                    open_remove -= 1
                else:
                    close_remove += 1
        results: set[str] = set()
        length = len(s)
        dfs(0, open_remove, close_remove, 0, 0, "")
        return list(results)
