class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        """Monotonic stack on circular array to find next greater elements.

        Intuition:
            By iterating through the array twice (simulating circular), we can
            use a monotonic stack to find the next greater element for each position.

        Approach:
            Traverse the array from right to left, doubled for circularity.
            Maintain a decreasing stack. For each element, pop smaller values
            and record the stack top as the next greater element.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(nums)
        result = [-1] * length
        stack: list[int] = []
        for i in range(length * 2 - 1, -1, -1):
            i %= length
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(nums[i])
        return result
