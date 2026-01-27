class Solution:
    def maximum69Number(self, num: int) -> int:
        """Maximize the number by changing at most one digit (6->9 or 9->6).

        Intuition:
            Changing the leftmost 6 to 9 yields the maximum possible value.

        Approach:
            Convert to string, replace the first occurrence of '6' with '9',
            and convert back to integer.

        Complexity:
            Time: O(d) where d is the number of digits
            Space: O(d)
        """
        return int(str(num).replace("6", "9", 1))
