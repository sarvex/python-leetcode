class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        """Maximize the minimum sweetness piece after dividing chocolate.

        Intuition:
            Binary search on the answer: the minimum sweetness value. For a
            given candidate, greedily count how many pieces of at least that
            sweetness can be formed.

        Approach:
            Binary search over the range [0, total_sweetness]. For each
            candidate mid, greedily split the array into contiguous pieces
            each having sweetness >= mid. If we can form more than k pieces,
            the candidate is feasible.

        Complexity:
            Time: O(n * log(sum(sweetness)))
            Space: O(1)
        """

        def can_divide(min_sweetness: int) -> bool:
            current_sum = piece_count = 0
            for value in sweetness:
                current_sum += value
                if current_sum >= min_sweetness:
                    current_sum = 0
                    piece_count += 1
            return piece_count > k

        left, right = 0, sum(sweetness)
        while left < right:
            mid = (left + right + 1) >> 1
            if can_divide(mid):
                left = mid
            else:
                right = mid - 1
        return left
