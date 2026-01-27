class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """Binary search on base for each possible digit count.

        Intuition:
            A 'good base' k for n means n = 1 + k + k^2 + ... + k^m. Try
            all possible digit counts m from largest to smallest, and binary
            search for the matching base.

        Approach:
            For each possible number of digits m (from 63 down to 2),
            binary search for a base k such that the geometric sum equals n.
            Return the first valid base found.

        Complexity:
            Time: O(log^2(n)) — log(n) possible digit counts, log(n) binary search
            Space: O(1)
        """

        def geometric_sum(base: int, digits: int) -> int:
            power = total = 1
            for _ in range(digits):
                power *= base
                total += power
            return total

        num = int(n)
        for digits in range(63, 1, -1):
            left, right = 2, num - 1
            while left < right:
                mid = (left + right) >> 1
                if geometric_sum(mid, digits) >= num:
                    right = mid
                else:
                    left = mid + 1
            if geometric_sum(left, digits) == num:
                return str(left)
        return str(num - 1)
