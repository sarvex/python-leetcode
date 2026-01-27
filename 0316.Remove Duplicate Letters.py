class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Monotonic stack approach for smallest lexicographic result.

        Intuition:
            Use a stack to build the result greedily. Pop characters from the
            stack if a smaller character comes and the popped character appears
            later in the string.

        Approach:
            1. Record the last occurrence index of each character.
            2. Iterate through the string, skipping already-used characters.
            3. While the stack top is greater than the current character and
               appears later, pop it and mark as unused.
            4. Push the current character and mark as used.

        Complexity:
            Time: O(n) where n is the length of s
            Space: O(1) since at most 26 characters in the stack
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack: list[str] = []
        visited: set[str] = set()
        for i, char in enumerate(s):
            if char in visited:
                continue
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return "".join(stack)
