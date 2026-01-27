class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        """Add integer k to the array-form of an integer.

        Intuition:
            Process digits from right to left, adding k digit by digit with
            carry propagation, similar to elementary addition.

        Approach:
            Iterate from the last digit of num and the least significant digit
            of k simultaneously, accumulating carry. Build the result in reverse
            then return it reversed.

        Complexity:
            Time: O(max(n, log k)) where n is the length of num
            Space: O(max(n, log k)) for the result
        """
        index, carry = len(num) - 1, 0
        result: list[int] = []
        while index >= 0 or k or carry:
            carry += (0 if index < 0 else num[index]) + (k % 10)
            carry, digit = divmod(carry, 10)
            result.append(digit)
            k //= 10
            index -= 1
        return result[::-1]
