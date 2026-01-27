class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """Find the length of the smallest repunit divisible by k.

        Intuition:
            A repunit of length n is (10^n - 1)/9. We can build it incrementally
            mod k. If a remainder repeats, no solution exists.

        Approach:
            Start with remainder 1 mod k and iteratively compute
            (remainder * 10 + 1) mod k. If remainder becomes 0, return the
            current length. By pigeonhole, if no solution in k steps, return -1.

        Complexity:
            Time: O(k) at most k iterations before a cycle
            Space: O(1)
        """
        remainder = 1 % k
        for length in range(1, k + 1):
            if remainder == 0:
                return length
            remainder = (remainder * 10 + 1) % k
        return -1
