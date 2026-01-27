class Solution:
    def brokenCalc(self, start_value: int, target: int) -> int:
        """Find minimum operations to reach target from start on broken calculator.

        Intuition:
            Working backwards from target is simpler: if target is odd we must
            have added 1, if even we can halve. This greedy reverse approach
            always yields the optimal number of steps.

        Approach:
            While target exceeds start_value, if target is odd increment it,
            otherwise halve it. Count each operation. Add the remaining
            difference when target falls below start_value.

        Complexity:
            Time: O(log(target)) since target is halved in most iterations
            Space: O(1)
        """
        operations = 0
        while start_value < target:
            if target & 1:
                target += 1
            else:
                target >>= 1
            operations += 1
        operations += start_value - target
        return operations
