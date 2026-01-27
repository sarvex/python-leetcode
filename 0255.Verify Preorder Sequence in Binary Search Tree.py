from math import inf


class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        """Monotonic stack simulation of BST preorder traversal.

        Intuition:
            In a valid BST preorder, when we encounter a value larger than
            the stack top, we are moving to a right subtree. All popped
            values establish a lower bound for subsequent elements.

        Approach:
            Maintain a decreasing stack. For each element, pop all smaller
            values (updating the lower bound). If any element is below the
            lower bound, the sequence is invalid.

        Complexity:
            Time: O(n) where n is the length of preorder
            Space: O(n) for the stack
        """
        stack: list[int] = []
        lower_bound = -inf
        for value in preorder:
            if value < lower_bound:
                return False
            while stack and stack[-1] < value:
                lower_bound = stack.pop()
            stack.append(value)
        return True
