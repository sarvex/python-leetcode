class Solution:
    def removeDuplicates(self, s: str) -> str:
        """Remove All Adjacent Duplicates In String using stack.

        Intuition:
            A stack naturally handles adjacent duplicate removal: push
            characters and pop when the top matches the current character.

        Approach:
            Iterate through the string. If the stack is non-empty and its
            top equals the current character, pop it. Otherwise, push the
            current character. The remaining stack forms the result.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        stack: list[str] = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
