class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """Simulate digit-by-digit addition from right to left.

        Intuition:
            Process both strings from the least significant digit, carrying
            overflow to the next position, just like manual addition.

        Approach:
            1. Start from the rightmost digits of both strings.
            2. Add corresponding digits with carry, compute quotient and remainder.
            3. Append remainder to result and continue until all digits processed.
            4. Reverse the result to get the final answer.

        Complexity:
            Time: O(max(m, n)) where m and n are the lengths of num1 and num2.
            Space: O(max(m, n)) for the result list.
        """
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        result = []
        carry = 0
        while idx1 >= 0 or idx2 >= 0 or carry:
            digit1 = 0 if idx1 < 0 else int(num1[idx1])
            digit2 = 0 if idx2 < 0 else int(num2[idx2])
            carry, value = divmod(digit1 + digit2 + carry, 10)
            result.append(str(value))
            idx1, idx2 = idx1 - 1, idx2 - 1
        return "".join(result[::-1])

    def subStrings(self, num1: str, num2: str) -> str:
        """Simulate digit-by-digit subtraction from right to left.

        Intuition:
            Subtract the smaller number from the larger, borrowing as needed.

        Approach:
            1. Determine if the result is negative by comparing lengths and values.
            2. Swap if needed so num1 >= num2.
            3. Subtract digit by digit with borrow, appending remainders.
            4. Strip leading zeros and prepend negative sign if needed.

        Complexity:
            Time: O(max(m, n)) where m and n are the lengths of num1 and num2.
            Space: O(max(m, n)) for the result list.
        """
        len1, len2 = len(num1), len(num2)
        negative = len1 < len2 or (len1 == len2 and num1 < num2)
        if negative:
            num1, num2 = num2, num1
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        result = []
        borrow = 0
        while idx1 >= 0:
            borrow = int(num1[idx1]) - borrow - (0 if idx2 < 0 else int(num2[idx2]))
            result.append(str((borrow + 10) % 10))
            borrow = 1 if borrow < 0 else 0
            idx1, idx2 = idx1 - 1, idx2 - 1
        while len(result) > 1 and result[-1] == "0":
            result.pop()
        if negative:
            result.append("-")
        return "".join(result[::-1])
