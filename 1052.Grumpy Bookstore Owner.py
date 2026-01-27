class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        """Maximize satisfied customers using a secret technique window.

        Intuition:
            Use a sliding window to find the best interval to suppress grumpiness.

        Approach:
            Slide a window of size `minutes` over grumpy intervals to maximize
            additional satisfied customers. Add the base satisfied count.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        max_gain = current_gain = sum(
            c * g for c, g in zip(customers[:minutes], grumpy)
        )
        for i in range(minutes, len(customers)):
            current_gain += customers[i] * grumpy[i]
            current_gain -= customers[i - minutes] * grumpy[i - minutes]
            max_gain = max(max_gain, current_gain)
        base_satisfied = sum(c * (g ^ 1) for c, g in zip(customers, grumpy))
        return base_satisfied + max_gain
