from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary search to find minimum eating speed.

        Intuition: The minimum eating speed must be between 1 and max(piles).
        We can use binary search to find the minimum valid speed.

        Approach: For each potential speed k, check if Koko can eat all bananas within h hours.
        The time to eat a pile is ceil(pile/k), which can be calculated as (pile + k - 1) // k.
        Use binary search to find the minimum valid k.

        Complexity:
        Time: O(n log m) where n is the length of piles and m is max(piles)
        Space: O(1) excluding input
        """
        left, right = 1, max(piles)

        def can_finish(speed: int) -> bool:
            """Check if Koko can eat all bananas within h hours at given speed."""
            hours_needed = sum((pile + speed - 1) // speed for pile in piles)
            return hours_needed <= h

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
