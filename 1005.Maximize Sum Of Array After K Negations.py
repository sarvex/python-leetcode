from collections import Counter


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        """Maximize array sum after negating exactly k elements.

        Intuition:
            Negate the most negative numbers first. If negations remain after all
            negatives are flipped, toggle the smallest absolute value element.

        Approach:
            Use a frequency counter. Iterate from -100 to -1 flipping negatives.
            If k remains odd and there is no zero, flip the smallest positive
            number once. Compute the weighted sum.

        Complexity:
            Time: O(n + C) where C=200 is the value range
            Space: O(C) for the counter
        """
        count: Counter[int] = Counter(nums)
        for value in range(-100, 0):
            if count[value]:
                flips = min(count[value], k)
                count[value] -= flips
                count[-value] += flips
                k -= flips
                if k == 0:
                    break
        if k & 1 and count[0] == 0:
            for value in range(1, 101):
                if count[value]:
                    count[value] -= 1
                    count[-value] += 1
                    break
        return sum(value * freq for value, freq in count.items())
