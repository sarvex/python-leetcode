class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        """Count subarrays where the first element is the minimum.

        Intuition:
            For each element, find the next smaller element using a monotonic stack
            to determine how many valid subarrays start at that position.

        Approach:
            Use a monotonic stack to compute the index of the next smaller element
            for each position. The count of valid subarrays starting at index i is
            next_smaller[i] - i.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        n = len(nums)
        next_smaller = [n] * n
        stack: list[int] = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        return sum(j - i for i, j in enumerate(next_smaller))
