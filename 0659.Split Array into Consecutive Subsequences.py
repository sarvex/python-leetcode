from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        """Greedy with min-heaps tracking subsequence lengths ending at each value.

        Intuition:
        For each number, try to extend the shortest existing subsequence ending at
        the previous value. If none exists, start a new subsequence of length 1.

        Approach:
        1. Use a dictionary mapping each value to a min-heap of subsequence lengths.
        2. For each number, if a subsequence ending at num-1 exists, extend it.
        3. Otherwise, start a new subsequence of length 1.
        4. After processing all numbers, check all subsequences have length >= 3.

        Complexity:
        Time: O(n log n)
        Space: O(n)
        """
        subsequences = defaultdict(list)
        for value in nums:
            if heap := subsequences[value - 1]:
                heappush(subsequences[value], heappop(heap) + 1)
            else:
                heappush(subsequences[value], 1)
        return all(not heap or heap and heap[0] > 2 for heap in subsequences.values())
