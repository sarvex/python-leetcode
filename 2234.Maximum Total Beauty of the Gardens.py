from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(
        self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        """
        Optimized greedy + prefix-costs to maximize full gardens and partial minimum.

        Intuition
        - Convert as many gardens as possible to "full" (>= target) to gain `full` points each.
        - For the remaining (non-full) gardens, distribute leftover flowers to maximize the minimum
          value among them (capped at target - 1) to gain `partial * min_value`.

        Approach
        - Early outs:
          1) If all gardens are already >= target, return full * n.
          2) If we can make all gardens full with available flowers, we can either make all full or
             leave one non-full at target - 1 for partial gain; take the max.
        - Sort `flowers`, strip those already >= target and count their full score `b`.
        - Build an array `even` where `even[j]` is the minimal cost to raise the first j+1 gardens
          to the same level as flowers[j]. This is computed via incremental differences.
        - Iterate from the end towards the start, at each step assuming we upgrade one more garden
          to full (consuming flowers accordingly). With the remaining flowers, binary search on
          `even` (using bisect_right) to find how high we can set the partial minimum among the
          first j+1 gardens, capped at target - 1. Track the maximum score.

        Complexity
        - Time: O(n log n) due to sorting and binary searches.
        - Space: O(n) for the prefix-costs array.
        """

        n: int = len(flowers)

        # Total deficit to bring all < target up to target.
        total_deficit: int = sum(target - f for f in flowers if f < target)
        if total_deficit == 0:
            return full * n
        if total_deficit <= newFlowers:
            # Either make all full, or leave one at target - 1 and take partial.
            return max(full * n, full * (n - 1) + partial * (target - 1))

        flowers.sort()

        # Count already-full gardens at the tail; accumulate base full score `b` and remove them.
        base_full_score: int = 0
        while flowers and flowers[-1] >= target:
            base_full_score += full
            flowers.pop()

        # If no gardens remain to consider for partial, we can only return the base score.
        if not flowers:
            return base_full_score

        # even[j] = minimal flowers needed to raise flowers[0..j] to flowers[j]
        even: List[int] = [0]
        running_cost: int = 0
        for i in range(1, len(flowers)):
            running_cost += i * (flowers[i] - flowers[i - 1])
            even.append(running_cost)

        max_beauty: int = 0
        remaining_flowers: int = newFlowers
        current_full_score: int = base_full_score

        # Iterate from the back; each step we try to make flowers[i] reach target (become full).
        for i in range(len(flowers) - 1, -1, -1):
            # With current remaining_flowers, maximize the partial minimum on the first (i+1) items.
            j: int = bisect_right(even, remaining_flowers, hi=i + 1) - 1
            # Height we can achieve for the first j+1 gardens.
            height: int = flowers[j] + (remaining_flowers - even[j]) // (j + 1)
            height = min(height, target - 1)
            max_beauty = max(max_beauty, current_full_score + partial * height)

            # Now try making flowers[i] full and move to next iteration.
            remaining_flowers -= max(0, target - flowers[i])
            if remaining_flowers < 0:
                break
            current_full_score += full

        return max_beauty
