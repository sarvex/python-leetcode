from math import inf


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """Monotonic stack scanning right-to-left to track the '2' element.

        Intuition:
            Scan from right to left maintaining a decreasing stack. The largest
            popped value becomes the candidate for '2' (middle element). If any
            element to the left is smaller than this candidate, we have a 132 pattern.

        Approach:
            1. Initialize the '2' candidate (second_max) to negative infinity.
            2. Traverse from right to left.
            3. If current < second_max, return True (found '1' < '2').
            4. While stack top < current, pop and update second_max (the '2').
            5. Push current onto the stack (candidate for '3').

        Complexity:
            Time: O(n) since each element is pushed and popped at most once.
            Space: O(n) for the stack.
        """
        second_max = -inf
        stack: list[int] = []
        for value in nums[::-1]:
            if value < second_max:
                return True
            while stack and stack[-1] < value:
                second_max = stack.pop()
            stack.append(value)
        return False
