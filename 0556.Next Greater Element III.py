class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """Find next greater permutation of digits using next permutation algorithm.

        Intuition:
            This is equivalent to finding the next permutation of the digit
            sequence. We find the rightmost digit that can be swapped with a
            larger digit to its right.

        Approach:
            1. Convert number to list of digit characters.
            2. Find the rightmost position i where digits[i] < digits[i+1].
            3. Find the rightmost position j where digits[j] > digits[i].
            4. Swap digits[i] and digits[j], then reverse the suffix after i.
            5. Return -1 if result exceeds 32-bit integer range.

        Complexity:
            Time: O(d) where d is the number of digits
            Space: O(d)
        """
        digits = list(str(n))
        length = len(digits)
        left, right = length - 2, length - 1
        while left >= 0 and digits[left] >= digits[left + 1]:
            left -= 1
        if left < 0:
            return -1
        while digits[left] >= digits[right]:
            right -= 1
        digits[left], digits[right] = digits[right], digits[left]
        digits[left + 1 :] = digits[left + 1 :][::-1]
        result = int("".join(digits))
        return -1 if result > 2**31 - 1 else result
