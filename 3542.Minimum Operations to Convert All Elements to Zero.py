from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Monotonic stack over zero-delimited segments

        Intuition:
        Treat each zero-delimited segment independently. Within a segment, we can zero all occurrences of the current minimum in one operation. As values rise and fall, each time we encounter a new strictly higher "level" (after removing larger levels via popping), we need one more operation.

        Approach:
        Scan left-to-right maintaining an increasing stack of positive levels for the current segment. On a zero, reset the stack. For a positive x, pop while stack top > x. If the stack is empty or top < x, push x and increment the answer. This counts exactly the number of value levels that must be cleared in order across all segments.

        Complexity:
        Time: O(n)
        Space: O(n) in the worst case for the stack
        """

        ans = 0
        stack: List[int] = []

        for x in nums:
            if x == 0:
                stack.clear()
                continue

            while stack and stack[-1] > x:
                stack.pop()

            if not stack or stack[-1] < x:
                stack.append(x)
                ans += 1

        return ans
