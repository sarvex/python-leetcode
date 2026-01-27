class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """Stack-based simulation to verify preorder serialization.

        Intuition:
            In a valid preorder serialization, every non-null node eventually
            gets two null children. We can collapse completed subtrees into
            null markers.

        Approach:
            1. Push each token onto a stack.
            2. Whenever the top two elements are '#' and the third is not '#',
               pop all three and push '#' (collapsing a complete subtree).
            3. A valid serialization reduces to a single '#'.

        Complexity:
            Time: O(n) where n is the number of tokens
            Space: O(n) for the stack
        """
        stack: list[str] = []
        for token in preorder.split(","):
            stack.append(token)
            while len(stack) > 2 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                stack = stack[:-3]
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"
