import math
from collections import deque
from itertools import accumulate


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """Monotonic deque on prefix sums to find shortest qualifying subarray.

        Intuition:
        Using prefix sums, the subarray sum from i to j equals prefix[j] - prefix[i].
        A monotonic deque maintains candidate starting indices in increasing
        prefix sum order, enabling efficient minimum-length search.

        Approach:
        1. Compute prefix sums with initial 0
        2. For each prefix sum, pop from front while current - front >= k
        3. Pop from back while back's prefix sum >= current (maintain monotonicity)
        4. Track the minimum window length found

        Complexity:
        Time: O(n) where n is the array length
        Space: O(n) for prefix sums and deque
        """
        prefix_sums = list(accumulate(nums, initial=0))
        index_deque: deque[int] = deque()
        min_length = math.inf
        for index, prefix_value in enumerate(prefix_sums):
            while index_deque and prefix_value - prefix_sums[index_deque[0]] >= k:
                min_length = min(min_length, index - index_deque.popleft())
            while index_deque and prefix_sums[index_deque[-1]] >= prefix_value:
                index_deque.pop()
            index_deque.append(index)
        return -1 if min_length == math.inf else int(min_length)
