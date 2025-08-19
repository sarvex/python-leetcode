class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Tagline: Sum n*(n+1)//2 for each contiguous zero-segment in a single pass.

        Intuition:
        Zero-filled subarrays within any run of length n equals 1 + 2 + ... + n = n*(n+1)//2.
        Summing this over all zero runs yields the total.

        Approach:
        Traverse once, count the current run length `run`. On a non-zero, add the closed run's
        contribution using `run*(run+1)//2` and reset. After the loop, add the final run if any.

        Complexity:
        Time: O(n)
        Space: O(1)
        """
        total = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
            elif run:
                total += (run * (run + 1)) // 2
                run = 0
        if run:
            total += (run * (run + 1)) // 2
        return total
