class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """Simulate stack operations to validate push/pop sequence.

        Intuition:
            Push elements one by one and greedily pop whenever the stack top
            matches the next expected pop value.

        Approach:
            1. Iterate through pushed elements, pushing each onto a stack.
            2. After each push, pop as many elements as possible that match
               the popped sequence in order.
            3. If all elements are popped successfully, the sequences are valid.

        Complexity:
            Time: O(n) — each element pushed and popped at most once
            Space: O(n) — stack storage
        """
        stack = []
        pop_index = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(popped)
