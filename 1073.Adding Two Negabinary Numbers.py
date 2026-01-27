class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """Add two numbers represented in base -2.

        Intuition:
            Similar to binary addition but carries propagate with negation
            due to base -2 arithmetic.

        Approach:
            Process digits right-to-left. Handle carry: if sum >= 2, subtract 2
            and carry -1; if sum == -1, set digit to 1 and carry +1.

        Complexity:
            Time: O(max(len(arr1), len(arr2)))
            Space: O(max(len(arr1), len(arr2))) for the result
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        result: list[int] = []
        while i >= 0 or j >= 0 or carry:
            digit_a = 0 if i < 0 else arr1[i]
            digit_b = 0 if j < 0 else arr2[j]
            total = digit_a + digit_b + carry
            carry = 0
            if total >= 2:
                total -= 2
                carry = -1
            elif total == -1:
                total = 1
                carry = 1
            result.append(total)
            i, j = i - 1, j - 1
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
