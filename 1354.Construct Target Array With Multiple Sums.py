from heapq import heapify, heappop, heappush


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        """Determine if target array can be constructed from all ones via repeated sums.

        Intuition:
            Work backwards: the largest element must have been the most recently
            replaced value. Subtract the rest-of-array sum to recover the
            previous value and repeat until all elements are one.

        Approach:
            Use a max-heap (negated values). Repeatedly extract the maximum,
            compute the remainder of the array sum, and replace the max with
            max mod remainder. If remainder is zero or the replacement is less
            than one, return False. Continue until the max is one.

        Complexity:
            Time: O(n log n + max_val * log n) in the worst case.
            Space: O(n)
        """
        total = sum(target)
        max_heap = [-x for x in target]
        heapify(max_heap)

        while -max_heap[0] > 1:
            maximum = -heappop(max_heap)
            rest = total - maximum
            if rest == 0 or maximum - rest < 1:
                return False
            replacement = (maximum % rest) or rest
            heappush(max_heap, -replacement)
            total = total - maximum + replacement

        return True
