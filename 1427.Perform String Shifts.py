class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        """Perform string shifts by net offset modulo length.

        Intuition:
            Left and right shifts cancel out, so compute the net shift amount.

        Approach:
            Sum all shift amounts treating direction 0 as negative (left) and
            direction 1 as positive (right). Take modulo of string length and
            slice accordingly.

        Complexity:
            Time: O(n + m) where n is string length and m is number of shifts
            Space: O(n) for the result string
        """
        net_shift = sum(
            (amount if direction else -amount) for direction, amount in shift
        )
        net_shift %= len(s)
        return s[-net_shift:] + s[:-net_shift]
