from bisect import bisect_left


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        """Binary search on answer with two-pointer counting.

        Intuition:
            The k-th smallest pair distance can be found by binary searching
            on the distance value and counting how many pairs have distance
            less than or equal to the candidate.

        Approach:
            1. Sort the array.
            2. Binary search on the distance range [0, max - min].
            3. For each candidate distance, count pairs with distance <= candidate
               using binary search on the sorted array.
            4. Find the smallest distance where the count reaches k.

        Complexity:
            Time: O(n * log(n) + n * log(W)) where W is max distance
            Space: O(n) for sorting
        """

        def count_pairs(max_distance: int) -> int:
            pair_count = 0
            for i, upper in enumerate(nums):
                lower = upper - max_distance
                left_index = bisect_left(nums, lower, 0, i)
                pair_count += i - left_index
            return pair_count

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count_pairs)
