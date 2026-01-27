from functools import reduce
from operator import xor


class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        """Game theory: Alice wins if XOR is 0 or array length is even.

        Intuition:
            If the XOR of all numbers is already 0, Alice wins immediately.
            Otherwise, with an even number of elements, Alice can always force
            a win by maintaining a non-zero XOR for Bob.

        Approach:
            1. If array length is even, Alice wins.
            2. Otherwise, check if the total XOR is already 0.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0
