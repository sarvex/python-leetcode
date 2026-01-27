class Solution:
    def maximumSwap(self, num: int) -> int:
        """Track rightmost largest digit suffix to find optimal swap.

        Intuition:
        For each position, know the index of the rightmost maximum digit from that
        position onward. Then find the first position where swapping with that
        maximum yields a larger number.

        Approach:
        1. Convert number to digit array.
        2. Build an array where best[i] = index of the largest digit from i to end (rightmost).
        3. Find the first position where digit < digit at best[i] and swap.

        Complexity:
        Time: O(n) where n is number of digits
        Space: O(n)
        """
        digits = list(str(num))
        length = len(digits)
        best_idx = list(range(length))
        for i in range(length - 2, -1, -1):
            if digits[i] <= digits[best_idx[i + 1]]:
                best_idx[i] = best_idx[i + 1]
        for i, j in enumerate(best_idx):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
                break
        return int("".join(digits))
