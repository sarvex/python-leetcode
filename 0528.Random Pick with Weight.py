import random


class Solution:
    """Weighted random pick using prefix sums and binary search.

    Intuition:
        Weights define the probability of picking each index. A prefix sum
        array maps uniform random numbers to weighted indices.

    Approach:
        Build prefix sums of weights. To pick, generate a random number in
        [1, total_weight] and binary search for the first prefix sum >= that number.

    Complexity:
        Time: O(n) for init, O(log n) for pickIndex
        Space: O(n)
    """

    def __init__(self, weights: list[int]) -> None:
        self.prefix_sums = [0]
        for weight in weights:
            self.prefix_sums.append(self.prefix_sums[-1] + weight)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])
        left, right = 1, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) >> 1
            if self.prefix_sums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left - 1
