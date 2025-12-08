from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Count the number of partitions where the sum difference is even.

        Mathematical explanation:
        Let S be the total sum of the array.
        Let L be the left sum and R be the right sum.
        We know that L + R = S, so R = S - L.

        We want to find partitions where (L - R) is even.
        Substituting R: (L - (S - L)) = 2L - S.

        We check if (2L - S) % 2 == 0.
        Since 2L is always even, the condition depends entirely on S:
        - If S is odd, (2L - S) is odd for ANY partition. Count = 0.
        - If S is even, (2L - S) is even for ANY partition. Count = Total partitions.

        The number of valid partitions is len(nums) - 1.

        Args:
            nums: List of integers to partition

        Returns:
            0 if total sum is odd, else (len(nums) - 1).
        """
        # If total sum is odd, difference is always odd.
        # If total sum is even, difference is always even.
        if sum(nums) % 2 == 1:
            return 0
        return len(nums) - 1
