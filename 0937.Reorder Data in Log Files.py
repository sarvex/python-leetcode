class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """Custom sort with letter logs before digit logs.

        Intuition:
            Letter logs should be sorted by content then identifier, while digit
            logs maintain their original relative order after all letter logs.

        Approach:
            1. Define a sort key that distinguishes letter vs digit logs.
            2. Letter logs get key (0, body, identifier) for proper ordering.
            3. Digit logs get key (1,) to stay after letters in original order.
            4. Python's stable sort preserves relative order of digit logs.

        Complexity:
            Time: O(n * m * log n) — sorting n logs of average length m
            Space: O(n * m) — for sort keys
        """

        def sort_key(log: str) -> tuple:
            identifier, body = log.split(" ", 1)
            return (0, body, identifier) if body[0].isalpha() else (1,)

        return sorted(logs, key=sort_key)
