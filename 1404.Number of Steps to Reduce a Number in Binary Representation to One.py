class Solution:
    def numSteps(self, s: str) -> int:
        """Count steps to reduce binary number to 1 (add 1 if odd, divide if even).

        Intuition:
            Process the binary string from least significant bit. Track carry
            to handle addition when the number is odd.

        Approach:
            Traverse from the rightmost bit to the second bit. Maintain a
            carry flag. If current bit (with carry) is 1, it takes 2 steps
            (add 1 + divide). If 0, it takes 1 step (divide). Handle final
            carry at the end.

        Complexity:
            Time: O(n) where n is the length of the binary string
            Space: O(1) auxiliary space
        """
        carry = False
        steps = 0
        for bit in s[:0:-1]:
            if carry:
                if bit == "0":
                    bit = "1"
                    carry = False
                else:
                    bit = "0"
            if bit == "1":
                steps += 1
                carry = True
            steps += 1
        if carry:
            steps += 1
        return steps
