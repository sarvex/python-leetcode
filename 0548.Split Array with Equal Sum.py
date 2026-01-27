class Solution:
    def splitArray(self, nums: list[int]) -> bool:
        """Split array into four equal-sum parts using prefix sums and hash set.

        Intuition:
            If we fix the middle partition index j, the left and right partitions
            can be checked independently. We use prefix sums to compute subarray
            sums in O(1) and a set to record valid left partition sums.

        Approach:
            1. Build a prefix sum array.
            2. Iterate j from 3 to n-4 as the middle partition index.
            3. For each j, collect all valid left partition sums into a set.
            4. Check if any right partition yields a sum that matches one in the set.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        length = len(nums)
        prefix = [0] * (length + 1)
        for i, val in enumerate(nums):
            prefix[i + 1] = prefix[i] + val
        for j in range(3, length - 3):
            seen = set()
            for i in range(1, j - 1):
                if prefix[i] == prefix[j] - prefix[i + 1]:
                    seen.add(prefix[i])
            for k in range(j + 2, length - 1):
                if (
                    prefix[length] - prefix[k + 1] == prefix[k] - prefix[j + 1]
                    and prefix[length] - prefix[k + 1] in seen
                ):
                    return True
        return False
