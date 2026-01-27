from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """Count subarrays with exactly k different integers.

        Intuition:
            Exactly k distinct = at most k distinct minus at most (k-1) distinct.
            For each right endpoint, compute the leftmost valid start for both
            constraints and take the difference.

        Approach:
            Define a helper that for a given max-distinct limit returns the
            earliest valid left index for each right index using a sliding window
            with a counter. The answer is the sum of differences between the two
            boundary arrays.

        Complexity:
            Time: O(n) with two sliding window passes
            Space: O(n) for the position arrays
        """

        def earliest_start(max_distinct: int) -> list[int]:
            positions = [0] * len(nums)
            count: Counter[int] = Counter()
            left = 0
            for right, value in enumerate(nums):
                count[value] += 1
                while len(count) > max_distinct:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        count.pop(nums[left])
                    left += 1
                positions[right] = left
            return positions

        return sum(a - b for a, b in zip(earliest_start(k - 1), earliest_start(k)))
