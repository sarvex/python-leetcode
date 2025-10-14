class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        """
        Check if there exists at least two adjacent increasing subarrays of size >= k.

        Intuition:
        - We need to find if there are at least two adjacent increasing subarrays of size >= k,
          or a single subarray of size >= 2k.

        Approach:
        1. First, identify all increasing subarrays in the given array
        2. For each increasing subarray, check if its length is at least 2k
        3. For each pair of adjacent increasing subarrays, check if their combined length meets the criteria
        4. Return True if any of the above conditions are met, else False

        Complexity:
        - Time: O(n), where n is the length of nums
        - Space: O(m), where m is the number of increasing subarrays (worst case O(n))
        """
        increasing, idx, nums_len = [], 0, len(nums)

        # Identify all increasing subarrays
        for i, (num1, num2) in enumerate(zip(nums, nums[1:])):
            if num1 >= num2:
                if i - idx + 1 >= k:
                    increasing.append((idx, i))
                idx = i + 1
        # Check the last subarray
        if nums_len - 1 - idx + 1 >= k:
            increasing.append((idx, nums_len - 1))

        # Check for a single subarray of length >= 2k
        for start, end in increasing:
            if end - start + 1 >= 2 * k:
                return True

        # Check for two adjacent subarrays each of length >= k
        for (_, end1), (start2, _) in zip(increasing, increasing[1:]):
            if start2 == end1 + 1:
                return True

        return False
