class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """Monotonic stack tracking chunk maximums.

        Intuition:
            Each chunk can be represented by its maximum value. When we encounter
            a value smaller than the top of the stack, we merge chunks by popping
            until the stack top is no longer greater than the current value.

        Approach:
            1. Maintain a stack of chunk maximums
            2. For each value, if it's >= stack top, start a new chunk
            3. Otherwise, save the current max, pop all chunks with max > value,
               then push the saved max back (merged chunk)
            4. The stack size is the number of chunks

        Complexity:
            Time: O(n) each element is pushed and popped at most once
            Space: O(n) for the stack
        """
        stack: list[int] = []
        for value in arr:
            if not stack or value >= stack[-1]:
                stack.append(value)
            else:
                chunk_max = stack.pop()
                while stack and stack[-1] > value:
                    stack.pop()
                stack.append(chunk_max)
        return len(stack)
