class Solution:
    def reachNumber(self, target: int) -> int:
        """Greedy step accumulation with parity check.

        Intuition:
            Summing 1+2+...+k gives a position; flipping any step i changes
            the sum by 2i. So we need sum >= |target| with (sum - target) even.

        Approach:
            1. Take the absolute value of target (symmetry).
            2. Keep adding steps until the running sum >= target and
               (sum - target) is even.

        Complexity:
            Time: O(sqrt(target))
            Space: O(1)
        """
        target = abs(target)
        running_sum = steps = 0
        while True:
            if running_sum >= target and (running_sum - target) % 2 == 0:
                return steps
            steps += 1
            running_sum += steps
