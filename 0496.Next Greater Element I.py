class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Monotonic stack to find next greater element for each value.

        Intuition:
            Use a monotonic decreasing stack on nums2 to precompute the next
            greater element for every value, then look up results for nums1.

        Approach:
            Iterate through nums2, maintaining a stack. When a value is greater
            than the stack top, pop and record the mapping. Finally, look up
            each element of nums1 in the mapping.

        Complexity:
            Time: O(n + m) where n = len(nums2), m = len(nums1)
            Space: O(n)
        """
        next_greater = {}
        stack: list[int] = []
        for value in nums2:
            while stack and stack[-1] < value:
                next_greater[stack.pop()] = value
            stack.append(value)
        return [next_greater.get(value, -1) for value in nums1]
