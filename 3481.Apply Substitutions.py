from typing import List

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        """
        Iterative approach for applying substitutions with cycle detection.

        Intuition:
        The recursive approach can lead to exponential time complexity due to repeated subproblems.
        We can optimize this by using an iterative approach with memoization.

        Approach:
        1. Build a mapping from keys to their replacements
        2. For each '%' delimited key in the text, iteratively resolve it until we get a value
        3. Use memoization to avoid recomputing the same keys
        4. Detect cycles to prevent infinite loops

        Complexity:
        Time: O(n * m) where n is the length of text and m is the maximum chain length
        Space: O(k) where k is the number of unique keys
        """
        # Build replacement mapping
        mapping = {key: value for key, value in replacements}

        # Memoization cache to store resolved values
        resolved = {}

        def resolve_key(key: str) -> str:
            """Resolve a key to its final value, handling cycles."""
            if key in resolved:
                return resolved[key]

            # Track visited keys to detect cycles
            visited = set()
            current = key

            # Follow the chain of replacements
            while current in mapping and current not in visited:
                visited.add(current)
                current = mapping[current]

                # If we've already resolved this value, use it
                if current in resolved:
                    resolved[key] = resolved[current]
                    return resolved[key]

            # Either reached a value not in mapping or detected a cycle
            resolved[key] = current
            return current

        # Process the text iteratively
        result = []
        i = 0
        while i < len(text):
            if text[i] == '%':
                # Find the closing '%'
                j = text.find('%', i + 1)
                if j != -1:
                    # Extract and resolve the key
                    key = text[i + 1:j]
                    resolved_value = resolve_key(key)
                    result.append(resolved_value)
                    i = j + 1
                else:
                    # Unmatched '%', treat as literal
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1

        return ''.join(result)
