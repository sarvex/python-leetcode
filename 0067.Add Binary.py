class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Binary addition using built-in conversion functions
Intuition:
Convert binary strings to integers, add them, and convert back to binary.
Approach:
1. Convert both binary strings to integers using int(x, 2)
2. Add the integers
3. Convert the sum back to binary using bin()
4. Remove the '0b' prefix from the binary representation
Complexity:
Time: O(n) where n is the length of the longer binary string
Space: O(1) for computation, O(n) for the result
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary_manual(self, a: str, b: str) -> str:
        """Binary addition using manual bit-by-bit calculation
Intuition:
Perform binary addition manually by iterating from right to left,
tracking carry as we would do in decimal addition.
Approach:
1. Start from the rightmost bits of both strings
2. Add bits along with any carry from previous addition
3. Compute the current bit of the result and the new carry
4. Continue until we process all bits from both strings
Complexity:
Time: O(max(m,n)) where m and n are lengths of input strings
Space: O(max(m,n)) for the result string
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])
