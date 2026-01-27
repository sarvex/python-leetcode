from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        """Greedy frequency matching sorted by absolute value.

        Intuition:
            Process numbers from smallest absolute value first. Each number x
            must pair with 2x. By handling smaller values first, we ensure
            correct pairing without conflicts.

        Approach:
            1. Count frequencies of all elements.
            2. Check zero count is even (zeros pair with themselves).
            3. Sort unique values by absolute value.
            4. For each value x, verify freq[2x] >= freq[x], then subtract.

        Complexity:
            Time: O(n log n) — sorting the keys
            Space: O(n) — frequency counter
        """
        freq = Counter(arr)
        if freq[0] & 1:
            return False
        for value in sorted(freq, key=abs):
            if freq[value << 1] < freq[value]:
                return False
            freq[value << 1] -= freq[value]
        return True
