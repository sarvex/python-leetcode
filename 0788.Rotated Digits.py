class Solution:
    def rotatedDigits(self, n: int) -> int:
        """Check each number for valid rotation producing a different number.

        Intuition:
            A number is a "good" rotated number if all its digits are valid
            (0,1,2,5,6,8,9) and the rotation produces a different number
            (contains at least one of 2,5,6,9).

        Approach:
            1. Define a rotation mapping where invalid digits map to -1
            2. For each number 1..n, build the rotated version digit by digit
            3. If any digit is invalid, skip; otherwise check if rotated != original

        Complexity:
            Time: O(n * log n) checking each number's digits
            Space: O(1)
        """

        def check(number: int) -> bool:
            rotated, original = 0, number
            place = 1
            while original:
                digit = original % 10
                if rotation_map[digit] == -1:
                    return False
                rotated = rotation_map[digit] * place + rotated
                place *= 10
                original //= 10
            return number != rotated

        rotation_map = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        return sum(check(i) for i in range(1, n + 1))
