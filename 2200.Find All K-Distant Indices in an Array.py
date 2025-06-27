from typing import List

class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        """Single-pass approach for finding K-distant indices.

        Intuition: Process the array once, keeping track of the minimum index to consider
        to avoid duplicates when ranges overlap.

        Approach:
        1. Maintain a result list and a pointer to the next index to consider
        2. When we find nums[j] == key, add all valid indices from max(next_index, j-k) to j+k
        3. Update the next index to j+k+1 to avoid duplicates in overlapping ranges

        Complexity:
        Time: O(n), where n is the length of nums (single pass)
        Space: O(n), for storing the result
        """
        result = []
        next_index = 0  # Next index to consider (avoids duplicates)
        n = len(nums)

        for j in range(n):
            if nums[j] == key:
                left = max(next_index, j - k)
                right = min(n - 1, j + k) + 1

                result.extend(range(left, right))

                next_index = right

        return result
