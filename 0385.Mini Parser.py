class Solution:
    def deserialize(self, s: str) -> "NestedInteger":
        """Recursive descent parsing of nested integer string.

        Intuition:
            The string has a recursive structure where brackets denote
            nesting. We can parse by tracking bracket depth and splitting
            at commas only at the top level.

        Approach:
            1. Handle empty/empty-list and plain integer base cases.
            2. For nested lists, iterate through characters tracking depth.
            3. When at depth 0 and hitting a comma or end bracket,
               recursively parse the substring between delimiters.

        Complexity:
            Time: O(n * d) where n is string length and d is nesting depth
            Space: O(n * d) for recursive call stack and substrings
        """
        if not s or s == "[]":
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))
        result = NestedInteger()
        depth, start = 0, 1
        for i in range(1, len(s)):
            if depth == 0 and (s[i] == "," or i == len(s) - 1):
                result.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == "[":
                depth += 1
            elif s[i] == "]":
                depth -= 1
        return result
