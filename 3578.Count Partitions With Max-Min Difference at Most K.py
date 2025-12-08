from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        Count the number of ways to partition nums into contiguous segments
        where each segment has max-min <= k.

        Optimized Approach: Sliding Window + Monotonic Deques
        - Use monotonic deques to maintain min/max in O(1) amortized time
        - mxQueue: monotonic decreasing deque (max at front)
        - mnQueue: monotonic increasing deque (min at front)
        - cnt: running sum of valid partition counts in current window
        - dp[i]: number of ways to partition nums[0:i]

        Time Complexity: O(n) - each element added/removed at most once
        Space Complexity: O(n)
        """
        left = 0
        cnt = 1  # Running sum of dp values in valid window
        MOD = 1_000_000_007

        # Monotonic deques for tracking min/max
        mxQueue = deque()  # Decreasing: max at front
        mnQueue = deque()  # Increasing: min at front
        dp = [cnt]  # dp[i] = ways to partition nums[0:i]

        for right, num in enumerate(nums):
            # Maintain decreasing deque for maximum
            while mxQueue and num > mxQueue[-1]:
                mxQueue.pop()

            # Maintain increasing deque for minimum
            while mnQueue and num < mnQueue[-1]:
                mnQueue.pop()

            mxQueue.append(num)
            mnQueue.append(num)

            # Shrink window while max-min constraint violated
            while mxQueue[0] - mnQueue[0] > k:
                cnt -= dp[left]

                # Remove left element from deques if it's at front
                if nums[left] == mxQueue[0]:
                    mxQueue.popleft()
                if nums[left] == mnQueue[0]:
                    mnQueue.popleft()

                left += 1

            # Store number of ways to partition up to position right+1
            dp.append(cnt)

            # Update running count for next iteration
            cnt *= 2
            cnt %= MOD

        return dp[-1] % MOD
