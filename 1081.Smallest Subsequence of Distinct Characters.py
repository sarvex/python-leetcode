class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """Find the lexicographically smallest subsequence with all distinct characters.

        Intuition:
            Use a monotonic stack to greedily build the smallest result, popping
            larger characters that appear later in the string.

        Approach:
            Track last occurrence of each character. Iterate through the string,
            skip already-included characters. Pop from stack when the top is
            larger and will appear again later.

        Complexity:
            Time: O(n)
            Space: O(n) for the stack and tracking sets
        """
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        stack: list[str] = []
        included: set[str] = set()
        for i, char in enumerate(s):
            if char in included:
                continue
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                included.remove(stack.pop())
            stack.append(char)
            included.add(char)
        return "".join(stack)
