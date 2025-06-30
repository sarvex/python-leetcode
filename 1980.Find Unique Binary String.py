from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """Cantor's diagonal argument to find a binary string not in the given list.

Intuition:
We can construct a string that differs from each input string in at least
one position by using Cantor's diagonal argument - take the ith bit from
the ith string and flip it.

Approach:
1. For each position i, look at the ith character of the ith string
2. Flip that bit (0->1, 1->0) to ensure our result differs at that position
3. This guarantees our constructed string is different from all input strings

Complexity:
Time: O(n) where n is the length of nums
Space: O(n) for the result string
        """
        return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))
