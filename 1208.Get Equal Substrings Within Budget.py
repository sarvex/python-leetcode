from itertools import accumulate


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """Find the maximum length substring that can be changed within budget.

        Intuition:
            The cost to change each character forms a prefix sum array. A valid
            substring of length mid exists if any window of that size has total
            cost within maxCost.

        Approach:
            Build a prefix sum of absolute character differences. Binary search
            on the answer length, checking each candidate via a sliding window
            over the prefix sum array.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """

        def check(mid: int) -> bool:
            for i in range(length):
                j = i + mid - 1
                if j < length and prefix[j + 1] - prefix[i] <= maxCost:
                    return True
            return False

        length = len(s)
        prefix = list(
            accumulate((abs(ord(a) - ord(b)) for a, b in zip(s, t)), initial=0)
        )
        left, right = 0, length
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
