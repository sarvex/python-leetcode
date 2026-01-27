class Solution:
    """
    1323. Maximum 69 Number

    Given a positive integer num consisting only of digits 6 and 9,
    return the maximum number you can get by changing at most one digit
    (6 becomes 9, and 9 becomes 6).

    Example 1: Input: num = 9669 -> Output: 9969
    Example 2: Input: num = 9996 -> Output: 9999
    Example 3: Input: num = 9999 -> Output: 9999
    """

    def maximum69Number(self, num: int) -> int:
        # Convert to string and replace first '6' with '9'
        return int(str(num).replace("6", "9", 1))

    def maximum69NumberMath(self, num: int) -> int:
        # Mathematical approach: find leftmost 6 and change it to 9
        temp = num
        position = -1
        current_pos = 0

        # Find the leftmost 6 by tracking all 6 positions
        while temp > 0:
            if temp % 10 == 6:
                position = current_pos
            temp //= 10
            current_pos += 1

        # If we found a 6, add 3 * 10^position to change 6 to 9
        if position >= 0:
            return num + 3 * (10**position)

        return num
