class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        Find the maximum frequency of any element after performing at most numOperations operations.
        Each operation can increase or decrease an element by 1.

        Intuition:
        - Sort the array to bring numbers closer to each other
        - Use sliding window to find the largest window where all elements can be made equal with at most k operations
        - Consider both cases: with and without using operations

        Approach:
        1. Sort the array to group similar numbers together
        2. Use sliding window to find the maximum window where elements can be made equal
        3. Handle both cases: when we use operations and when we don't
        4. Return the maximum frequency found

        Complexity:
        - Time: O(n log n) due to sorting, where n is the length of nums
        - Space: O(1) as we use constant extra space
        """
        nums.sort()
        n = len(nums)
        res = 0
        left = 0
        right = 0
        i = 0

        # First pass: find maximum frequency when we can use operations
        while i < n:
            x = nums[i]
            j = i
            cnt_x = 0
            # Count occurrences of current number x
            while j < n and nums[j] == x:
                cnt_x += 1
                j += 1
            # Find the left boundary where nums[left] >= x - k
            while left < n and nums[left] < x - k:
                left += 1
            # Find the right boundary where nums[right] > x + k
            while right < n and nums[right] <= x + k:
                right += 1
            # Update result with minimum of (window size, count of x + operations)
            res = max(res, min(right - left, cnt_x + numOperations))
            i = j

        # If we already have enough operations to make all elements equal to the most frequent one
        if res >= n:
            return n

        # Second pass: find maximum frequency without using operations
        res_no_ops = 0
        left = 0
        for right, x in enumerate(nums):
            # Maintain window where all elements can be made equal to x with at most k operations
            while nums[left] < x - k * 2:
                left += 1
            res_no_ops = max(res_no_ops, right - left + 1)

        # The final result is the maximum between using operations and not using them
        return max(res, min(res_no_ops, numOperations))
