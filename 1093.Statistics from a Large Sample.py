import math


class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        """Compute sample statistics from frequency array.

        Intuition:
            With a frequency count array indexed by value 0-255, we can derive
            min, max, mean, median, and mode in a single pass plus a helper
            function to find the k-th element.

        Approach:
            Iterate through the count array to find min, max, total sum, total
            count, and mode. Use a helper that accumulates frequencies to locate
            the k-th smallest element for median computation.

        Complexity:
            Time: O(n) where n is the length of count (256)
            Space: O(1)
        """

        def find_kth(target: int) -> int:
            cumulative = 0
            for value, freq in enumerate(count):
                cumulative += freq
                if cumulative >= target:
                    return value
            return 0

        minimum: float = math.inf
        maximum = -1
        total_sum = total_count = 0
        mode = 0
        for value, freq in enumerate(count):
            if freq:
                minimum = min(minimum, value)
                maximum = max(maximum, value)
                total_sum += value * freq
                total_count += freq
                if freq > count[mode]:
                    mode = value

        if total_count & 1:
            median = find_kth(total_count // 2 + 1)
        else:
            median = (find_kth(total_count // 2) + find_kth(total_count // 2 + 1)) / 2
        return [minimum, maximum, total_sum / total_count, median, mode]
